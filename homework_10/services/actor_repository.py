import sqlite3
from homework.homework_10.services.actor import Actor
from typing import List, Tuple, Optional


class ActorRepository:
    """
    Repository class for managing Actor records in the database.
    Provides methods to save, retrieve, delete, and search actors,
    as well as assign them to films.
    """

    def __init__(self, db_name: str = "cinemabase.db") -> None:
        """
        Initializes the repository with a database connection.

        :param db_name: Name of the database file.
        """
        self.actors: List[Actor] = []
        self.connection: sqlite3.Connection = sqlite3.connect(db_name)
        self.cursor: sqlite3.Cursor = self.connection.cursor()

    def save(self, actor: Actor) -> None:
        """
        Saves an actor record in the database.

        :param actor: Actor instance to be saved.
        """
        self.cursor.execute(
            "INSERT INTO actors (name, birth_year) VALUES (?, ?)",
            tuple(el[1] for el in actor.items())
        )
        self.connection.commit()

    def get_all(self) -> List[Tuple]:
        """
        Retrieves all actors from the database.

        :return: List of all actor records.
        """
        self.cursor.execute("SELECT * FROM actors")
        return self.cursor.fetchall()

    def get_by_id(self, id: int) -> Optional[Tuple]:
        """
        Retrieves an actor by their ID.

        :param id: Actor ID.
        :return: Actor record if found, else None.
        """
        self.cursor.execute("SELECT * FROM actors WHERE id = ?", (id,))
        return self.cursor.fetchone()

    def delete(self, id: int) -> None:
        """
        Deletes an actor record from the database.

        :param id: Actor ID to delete.
        """
        self.cursor.execute("DELETE FROM actors WHERE id = ?", (id,))
        self.connection.commit()

    def search_by_name(self, name: str) -> List[Tuple]:
        """
        Searches for actors by name.

        :param name: Actor name to search for.
        :return: List of matching actor records.
        """
        self.cursor.execute("SELECT * FROM actors WHERE name LIKE ?", (f"%{name}%",))
        return self.cursor.fetchall()

    def assign_actor_to_film(self, actor_id: int, film_id: int) -> None:
        """
        Assigns an actor to a film by inserting a record into the movie_cast table.

        :param actor_id: ID of the actor.
        :param film_id: ID of the film.
        """
        self.cursor.execute(
            "INSERT INTO movie_cast (actor_id, movie_id) VALUES (?, ?)", (actor_id, film_id)
        )
        self.connection.commit()

    def close_connection(self) -> None:
        """
        Closes the database connection.
        """
        self.connection.close()