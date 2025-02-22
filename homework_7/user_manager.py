import pytest


class UserManager:
    def __init__(self):
        self.users = {}

    def add_user(self, name: str, age: int):
        self.users[name] = age

    def remove_user(self, name: str):
        if name in self.users:
            del self.users[name]

    def get_all_users(self) -> list:
        return list(self.users.items())


@pytest.fixture
def user_manager():
    um = UserManager()
    um.add_user("Alice", 30)
    um.add_user("Bob", 25)
    return um


def test_add_user(user_manager):
    user_manager.add_user("Charlie", 40)
    assert ("Charlie", 40) in user_manager.get_all_users()


def test_remove_user(user_manager):
    user_manager.remove_user("Alice")
    assert ("Alice", 30) not in user_manager.get_all_users()


def test_get_all_users(user_manager):
    users = user_manager.get_all_users()
    assert len(users) == 2
    assert ("Alice", 30) in users
    assert ("Bob", 25) in users


@pytest.mark.skipif(len(user_manager().get_all_users()) < 3, reason="Not enough users to test")
def test_skip_if_few_users(user_manager):
    assert len(user_manager.get_all_users()) >= 3
