import sqlite3
from typing import List, Tuple, Optional
from homework.homework_10.services.movie import Movie


class MovieRepository:
    """
    Repository class for managing Movie records in the database.
    Provides methods to save, retrieve, delete, and search movies,
    as well as retrieve unique genres and calculate average age by genre.
    """

    def __init__(self, db_name: str = "cinemabase.db") -> None:
        """
        Initializes the repository with a database connection.

        :param db_name: Name of the database file.
        """
        self.connection: sqlite3.Connection = sqlite3.connect(db_name)
        self.cursor: sqlite3.Cursor = self.connection.cursor()

    def save(self, movie: Movie) -> None:
        """
        Saves a movie record in the database.

        :param movie: Movie instance to be saved.
        """
        self.cursor.execute(
            "INSERT INTO movies (title, release_year, genre) VALUES (?, ?, ?)",
            tuple(el[1] for el in movie.items())
        )
        self.connection.commit()

    def get_all(self, page: Optional[int] = None, limit: int = 7) -> List[Tuple]:
        """
        Retrieves all movies from the database with optional pagination.

        :param page: Page number for pagination.
        :param limit: Number of results per page.
        :return: List of movie records.
        """
        offset = (page - 1) * limit if page else 0
        self.cursor.execute("SELECT * FROM movies LIMIT ? OFFSET ?", (limit, offset))
        return self.cursor.fetchall()

    def get_by_id(self, id: int) -> Optional[Tuple]:
        """
        Retrieves a movie by its ID.

        :param id: Movie ID.
        :return: Movie record if found, else None.
        """
        self.cursor.execute("SELECT * FROM movies WHERE id = ?", (id,))
        return self.cursor.fetchone()

    def delete(self, id: int) -> None:
        """
        Deletes a movie record from the database.

        :param id: Movie ID to delete.
        """
        self.cursor.execute("DELETE FROM movies WHERE id = ?", (id,))
        self.connection.commit()

    def search_by_genre(self, genre: str) -> List[Tuple]:
        """
        Searches for movies by genre.

        :param genre: Movie genre to search for.
        :return: List of matching movie records.
        """
        self.cursor.execute("SELECT * FROM movies WHERE genre = ?", (genre,))
        return self.cursor.fetchall()

    def get_unique_genres(self) -> List[Tuple]:
        """
        Retrieves all unique genres from the movies table.

        :return: List of unique genres.
        """
        self.cursor.execute("SELECT DISTINCT genre FROM movies")
        return self.cursor.fetchall()

    def search_by_title(self, name: str) -> List[Tuple]:
        """
        Searches for movies by an actor's name.

        :param name: Actor's name to search for.
        :return: List of matching movie records.
        """
        self.cursor.execute(
            """
            SELECT * FROM movies m
            INNER JOIN movie_cast mc ON m.id = mc.movie_id
            INNER JOIN actors a ON mc.actor_id = a.id
            WHERE a.name LIKE ?
            """,
            (f"%{name}%",)
        )
        return self.cursor.fetchall()

    def show_average_age_by_genre(self, genre: str) -> Optional[Tuple]:
        """
        Calculates the average birth year of actors in movies of a given genre.

        :param genre: Movie genre to analyze.
        :return: The average birth year of actors in that genre.
        """
        self.cursor.execute(
            """
            SELECT m.genre, AVG(a.birth_year)
            FROM movies m
            INNER JOIN movie_cast mc ON m.id = mc.movie_id
            INNER JOIN actors a ON mc.actor_id = a.id
            WHERE m.genre = ?
            GROUP BY m.genre
            """,
            (genre,)
        )
        return self.cursor.fetchone()

    def close_connection(self) -> None:
        """
        Closes the database connection.
        """
        self.connection.close()
