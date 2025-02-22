
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



