"""
Lab 19: API Requests and Caching

Fetch cryptocurrency prices from CoinGecko and cache them locally.
"""

import time
import requests


# CoinGecko API base URL
BASE_URL = "https://api.coingecko.com/api/v3"


def get_price(coin_id: str, api_key: str) -> float:
    response = requests.get(
        BASE_URL + "/simple/price",
        params={
            "ids": coin_id,
            "vs_currencies": "usd",
            "x_cg_demo_api_key": api_key
        }
    )

    if response.status_code != 200:
        raise RuntimeError(f"API request failed with status {response.status_code}")

    data = response.json()
    return float(data[coin_id]["usd"])

def get_prices_batch(coin_ids: list, api_key: str) -> dict:
    ids_string = ",".join(coin_ids)

    response = requests.get(
        BASE_URL + "/simple/price",
        params={
            "ids": ids_string,
            "vs_currencies": "usd",
            "x_cg_demo_api_key": api_key
        }
    )

    if response.status_code != 200:
        raise RuntimeError(f"API request failed with status {response.status_code}")

    data = response.json()

    result = {}
    for coin in coin_ids:
        result[coin] = float(data[coin]["usd"])

    return result


class CoinCache:
    def __init__(self, ttl_seconds: int = 60):
        self.ttl_seconds = ttl_seconds
        self._store = {}
        self.hits = 0
        self.misses = 0

    def put(self, coin_id: str, price: float):
        self._store[coin_id] = {
            "price": price,
            "timestamp": time.time()
        }

    def get(self, coin_id: str):
        if coin_id not in self._store:
            self.misses += 1
            return None

        entry = self._store[coin_id]
        current_time = time.time()

        # TTL check
        if current_time - entry["timestamp"] > self.ttl_seconds:
            self.misses += 1
            return None

        self.hits += 1
        return entry["price"]


def get_price_cached(coin_id: str, api_key: str, cache: CoinCache) -> float:
    cached = cache.get(coin_id)

    if cached is not None:
        return cached

    price = get_price(coin_id, api_key)
    cache.put(coin_id, price)
    return price