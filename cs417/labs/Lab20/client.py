"""Lab 20: Build the Other Side — Client

Client functions that talk to your FastAPI server. Each task adds
a new function that handles a more realistic scenario.
"""

import requests
import time


def submit(student: str, lab: int, base_url: str = "http://localhost:8000") -> dict:
    # TODO: Implement
    url = f"{base_url}/grade"

    response = requests.post(url, json={"student": student, "lab": lab})

    if response.status_code != 200:
        raise RuntimeError("request failed")

    return response.json()


def submit_with_retry(
    student: str,
    lab: int,
    base_url: str = "http://localhost:8000",
    timeout: float = 2,
    max_retries: int = 3,
) -> dict:
    # TODO: Implement
    url = f"{base_url}/grade"

    for _ in range(max_retries):
        try:
            response = requests.post(
                url,
                json={"student": student, "lab": lab, "slow": True},
                timeout=timeout,
            )

            if response.status_code == 200:
                return response.json()

        except requests.exceptions.Timeout:
            continue

    raise RuntimeError("all retries failed")


def submit_idempotent(
    student: str,
    lab: int,
    base_url: str = "http://localhost:8000",
    timeout: float = 2,
    max_retries: int = 3,
) -> dict:
    # TODO: Implement
    url = f"{base_url}/grade"
    submission_id = f"{student}-lab{lab}"

    for _ in range(max_retries):
        try:
            response = requests.post(
                url,
                json={
                    "student": student,
                    "lab": lab,
                    "slow": True,
                    "submission_id": submission_id,
                },
                timeout=timeout,
            )

            if response.status_code == 200:
                return response.json()

        except requests.exceptions.Timeout:
            continue

    raise RuntimeError("all retries failed")


def submit_async(
    student: str,
    lab: int,
    base_url: str = "http://localhost:8000",
    poll_interval: float = 0.5,
    max_polls: int = 20,
) -> dict:
    # TODO: Implement
    submission_id = f"{student}-lab{lab}"

    response = requests.post(
        f"{base_url}/grade-async",
        json={"student": student, "lab": lab, "submission_id": submission_id},
    )

    if response.status_code != 202:
        raise RuntimeError("failed to start async job")

    job_id = response.json()["job_id"]

    for _ in range(max_polls):
        time.sleep(poll_interval)

        res = requests.get(f"{base_url}/grade-jobs/{job_id}")
        data = res.json()

        if data["status"] == "complete":
            return data["result"]

    raise RuntimeError("polling timed out")


# ---------------------------------------------------------------------------
# Bonus Task 5: The Smart Client
# ---------------------------------------------------------------------------


class SmartClient:
    def __init__(self, base_url: str = "http://localhost:8000", timeout: float = 2):
        # TODO: Implement
        self.base_url = base_url
        self.timeout = timeout

    def submit(self, student: str, lab: int) -> dict:
        # TODO: Implement
        submission_id = f"{student}-lab{lab}"

        try:
            response = requests.post(
                f"{self.base_url}/grade",
                json={
                    "student": student,
                    "lab": lab,
                    "submission_id": submission_id,
                },
                timeout=self.timeout,
            )

            if response.status_code == 200:
                return response.json()

        except requests.exceptions.Timeout:
            pass

        return submit_async(student, lab, self.base_url)