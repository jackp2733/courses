from typing import TypedDict

# Section 1
def greet(name: str) -> str:
    return f"Hello, {name}!"

def square(n: int) -> int:
    return n * n

def is_adult(age: int) -> bool:
    return age >= 18

def log_message(msg: str) -> None:
    print(f"[log] {msg}")


# Section 2
def total_grades(grades: list[int]) -> int:
    return sum(grades)

def grade_lookup(roster: dict[str, int], name: str) -> int:
    return roster[name]

def first_and_last(items: list[str]) -> tuple[str, str]:
    return items[0], items[-1]


# Section 3
def find_grade(roster: dict[str, int], name: str) -> int | None:
    if name in roster:
        return roster[name]
    return None


# Section 4
class StudentRow(TypedDict):
    name: str
    email: str
    grade: str

def read_roster(path: str) -> list[StudentRow]:
    return [{"name": "Alice", "email": "alice@uni.edu", "grade": "92"}]


# Section 5
class User(TypedDict):
    id: int
    name: str

def make_badge(user: User) -> str:
    return f"#{user['id']}-{user['name']}"