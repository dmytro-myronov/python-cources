import asyncio
import requests


class AsyncFetcher:
    """
    A class to fetch data asynchronously with a delay before making a request.

    Methods
    -------
    say_hello:
        Prints a message, waits for 3 seconds, and then makes an HTTP request to Google.
    """

    async def say_hello(self):
        """
        Simulate an asynchronous action by waiting 3 seconds before making a request to Google.

        This function waits for 3 seconds, then sends an HTTP GET request to 'https://google.com'.
        It prints the response status code once the request is completed.
        """
        print("wait 3 sec before request to google")
        await asyncio.sleep(3)  # Wait for 3 seconds
        print("send request to google")
        google = requests.get("https://google.com")  # Make the HTTP request to Google
        status = google.status_code  # Get the status code from the response
        print(f"status {status}")  # Print the status code


async def main():
    """
    The main entry point of the program. Creates an instance of AsyncFetcher and calls the
    `say_hello` method asynchronously.
    """
    greeter = AsyncFetcher()  # Create an instance of AsyncFetcher
    await greeter.say_hello()  # Await the async method say_hello


# Run the main function asynchronously
asyncio.run(main())



from typing import Callable

def square(x: int) -> int:
    return x ** 2

def double(x: int) -> int:
    return x * 2

def apply_operation(x: int, operation: Callable[[int], int]) -> int:
    return operation(x)

print(apply_operation(5, square))  # 25
print(apply_operation(5, double))  # 10



def calculate_discount(price, discount):
    if discount > 100:
        return 0
    return price - (price * discount / 100)


price = 120
discount = 10
print(calculate_discount(price, discount))



def filter_adults(students: list[str, int]):
   return [student for student in students if student[1] >= 18]


people = [("Андрій", 25), ("Олег", 16), ("Марія", 19), ("Ірина", 15)]
print(filter_adults(people))



class Processor:
    def __init__(self, data):
        self.data = data

    def apply(self, callable):
        return list(map(callable, self.data))


p1 = Processor([1, 2, 3])
print(p1.apply(lambda x: x * 2))  # [2, 4, 6]

p2 = Processor(["hello", "world"])
print(p2.apply(str.upper))  # ["HELLO", "WORLD"]



from typing import List, TypeVar
def get_first(lst: List) -> object:
    return lst[0] if lst else None


print(get_first([1, 2, 3]))       # 1
print(get_first(["a", "b", "c"])) # "a"
print(get_first([]))              # None



from typing import Dict, Any
from abc import ABC, abstractmethod
from typing import final

@final
class Config:
    """
    Class that contains configuration.
    Declared as final, so it cannot be inherited.
    """
    DATABASE_URL = "sqlite:///:memory:"

class BaseRepository(ABC):
    """
    Abstract class that defines the interface for repositories.
    """
    @abstractmethod
    def save(self, data: Dict[str, Any]) -> None:
        """
        Saves data to the repository.
        :param data: Dictionary containing data to be saved.
        """
        pass

class SQLRepository(BaseRepository):
    """
    Implementation of a repository for working with an SQL database.
    """
    def save(self, data: Dict[str, Any]) -> None:
        """
        Saves data to an SQL database.
        :param data: Dictionary containing data to be saved.
        """
        print(f"Saving data to SQL database: {data}")

# Example usage
repo = SQLRepository()
repo.save({"name": "Product1", "price": 10.5})


from typing import Union


def parse_input(input_string: Union[int, str]) -> Union[int, None]:
    if isinstance(input_string, str):
        try:
            int_value = int(input_string)
            return int_value
        except ValueError:
            return  None

    elif isinstance(input_string, int):
        return input_string
    else:
        return None




print(parse_input(42))       # 42
print(parse_input("100"))    # 100
print(parse_input("hello"))  # None
print(parse_input(2.3))  # None





from typing import TypedDict
class User(TypedDict):
    id: int
    name: str
    is_admin: bool


class Protocol:
    def get_user(user_id: int) -> User:
        pass

    def save_user(user: User) -> None:
        pass

class InMemoryUserDb(Protocol):

    def __init__(self):
        self.list_users:User = []

    def get_user(self, user_id: int) -> User:
        for user in self.list_users:
            if user["id"] == user_id:
                return user


    def save_user(self, user: User) -> None:
        self.list_users.append(user)

db = InMemoryUserDb()
user1:User = {"id": 1, "name": "Alice", "is_admin": False}
user2 = {"id": 2, "name": "Bob", "is_admin": True}
db.save_user(user1)
db.save_user(user2)
print(db.get_user(1))



