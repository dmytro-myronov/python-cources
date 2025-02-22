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
