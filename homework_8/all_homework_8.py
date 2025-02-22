import asyncio
import requests
from typing import Callable, List, Dict, Any, Union, TypedDict, Protocol
from abc import ABC, abstractmethod


class AsyncFetcher:
    """
    A class to fetch data asynchronously with a delay before making a request.
    """

    async def say_hello(self) -> None:
        """
        Simulate an asynchronous action by waiting 3 seconds before making a request to Google.
        """
        print("Waiting 3 seconds before sending request to Google...")
        await asyncio.sleep(3)
        print("Sending request to Google")
        try:
            response = requests.get("https://google.com", timeout=5)
            print(f"Response status: {response.status_code}")
        except requests.RequestException as e:
            print(f"Request failed: {e}")


async def main() -> None:
    """
    Main entry point of the program.
    """
    fetcher = AsyncFetcher()
    await fetcher.say_hello()


if __name__ == "__main__":
    asyncio.run(main())


# Function application example
def square(x: int) -> int:
    return x ** 2


def double(x: int) -> int:
    return x * 2


def apply_operation(x: int, operation: Callable[[int], int]) -> int:
    return operation(x)


print(apply_operation(5, square))  # 25
print(apply_operation(5, double))  # 10


# Discount calculation
def calculate_discount(price: float, discount: float) -> float:
    """Calculate discounted price, ensuring discount does not exceed 100%."""
    return max(price - (price * min(discount, 100) / 100), 0)


print(calculate_discount(120, 10))  # 108.0


# Filtering adults
def filter_adults(students: List[tuple[str, int]]) -> List[tuple[str, int]]:
    return [student for student in students if student[1] >= 18]


people = [("Андрій", 25), ("Олег", 16), ("Марія", 19), ("Ірина", 15)]
print(filter_adults(people))


# Processor class
class Processor:
    def __init__(self, data: List[Any]) -> None:
        self.data = data

    def apply(self, func: Callable[[Any], Any]) -> List[Any]:
        return list(map(func, self.data))


p1 = Processor([1, 2, 3])
print(p1.apply(lambda x: x * 2))  # [2, 4, 6]

p2 = Processor(["hello", "world"])
print(p2.apply(str.upper))  # ["HELLO", "WORLD"]


# Get first element
def get_first(lst: List[Any]) -> Any:
    return lst[0] if lst else None


print(get_first([1, 2, 3]))       # 1
print(get_first(["a", "b", "c"])) # "a"
print(get_first([]))              # None


# Configuration and Repository classes
class Config:
    """Configuration class marked as final."""
    DATABASE_URL = "sqlite:///:memory:"


class BaseRepository(ABC):
    """Abstract repository base class."""

    @abstractmethod
    def save(self, data: Dict[str, Any]) -> None:
        pass


class SQLRepository(BaseRepository):
    """SQL repository implementation."""

    def save(self, data: Dict[str, Any]) -> None:
        print(f"Saving data to SQL database: {data}")


repo = SQLRepository()
repo.save({"name": "Product1", "price": 10.5})


# Input parsing
def parse_input(input_value: Union[int, str]) -> Union[int, None]:
    """Parse input and return an integer if possible."""
    if isinstance(input_value, int):
        return input_value
    if isinstance(input_value, str):
        try:
            return int(input_value)
        except ValueError:
            return None
    return None


print(parse_input(42))       # 42
print(parse_input("100"))    # 100
print(parse_input("hello"))  # None



# User Database
class User(TypedDict):
    id: int
    name: str
    is_admin: bool


class UserDatabase(Protocol):
    def get_user(self, user_id: int) -> Union[User, None]:
        pass

    def save_user(self, user: User) -> None:
        pass


class InMemoryUserDb(UserDatabase):
    def __init__(self) -> None:
        self.list_users: List[User] = []

    def get_user(self, user_id: int) -> Union[User, None]:
        return next((user for user in self.list_users if user["id"] == user_id), None)

    def save_user(self, user: User) -> None:
        self.list_users.append(user)


db = InMemoryUserDb()
user1: User = {"id": 1, "name": "Alice", "is_admin": False}
user2: User = {"id": 2, "name": "Bob", "is_admin": True}
db.save_user(user1)
db.save_user(user2)
print(db.get_user(1))
