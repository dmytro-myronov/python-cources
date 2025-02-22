import math
from homework.homework_10.install_db_cinemabase import create_tables
import services


def main() -> None:
    page_limit = 7
    """
    Main function to handle user input and execute corresponding actions.
    """
    try:
        task = int(input(
            """
            1) Add new film
            2) Show all films
            3) Delete film
            4) Add new actor
            5) Show all actors
            6) Delete actor
            7) Show all films with actors (provide actor's name to search or leave empty to show all films with actors)
            8) Show unique genres
            9) Show average age of actors by film genre
            10) Search film by name
            11) Assign actor to film
            12) Show all films with pagination
            Please choose a task: """
        ))

        movie_repository = services.MovieRepository()
        actor_repository = services.ActorRepository()

        if task == 1:
            film = input("Please add new film name: ")
            film_release_year = int(input("Please add new film release year: "))
            film_genre = input("Please add new film genre: ")

            movie = {"title": film, "release_year": film_release_year, "genre": film_genre}
            movie_repository.save(movie)
            print("Film added successfully.")

        elif task == 2:
            for movie in movie_repository.get_all():
                print(movie)

        elif task == 3:
            film_id = int(input("Please enter film ID: "))
            movie_repository.delete(film_id)
            print("Film deleted successfully.")

        elif task == 4:
            actor_name = input("Please add new actor name: ")
            actor_birth_year = int(input("Please add new actor birth year: "))

            actor = {"name": actor_name, "birth_year": actor_birth_year}
            actor_repository.save(actor)
            print("Actor added successfully.")

        elif task == 5:
            for actor in actor_repository.get_all():
                print(actor)

        elif task == 6:
            actor_id = int(input("Please enter actor ID: "))
            actor_repository.delete(actor_id)
            print("Actor deleted successfully.")

        elif task == 7:
            actors_name = input("Please enter actor's name to search or leave empty to show all films with actors: ")
            movies = movie_repository.search_by_title(actors_name) if actors_name else movie_repository.get_all()
            for movie in movies:
                print(movie)

        elif task == 8:
            for genre in movie_repository.get_unique_genres():
                print(genre)

        elif task == 9:
            genre = input("Please enter genre: ")
            average_age = movie_repository.show_average_age_by_genre(genre)
            if average_age:
                print(f"{genre}: {average_age[1]}")
            else:
                print("No data available for the selected genre.")

        elif task == 10:
            film_name = input("Please enter film name: ")
            movies = movie_repository.search_by_title(film_name)
            for movie in movies:
                print(movie)

        elif task == 11:
            movie_id = int(input("Please enter movie ID: "))
            actor_id = int(input("Please enter actor ID: "))
            actor_repository.assign_actor_to_film(actor_id, movie_id)
            print("Actor assigned to film successfully.")

        elif task == 12:
            all_movies = movie_repository.get_all(limit=-1)
            total_pages = math.ceil(len(all_movies) / page_limit)
            print(f"Total pages: {total_pages}")
            s_page = int(input("Provide the page number you need: "))
            movies = movie_repository.get_all(s_page, page_limit)
            for movie in movies:
                print(movie)

    except ValueError:
        print("Invalid input. Please enter a number corresponding to the task.")
    except Exception as e:
        print("Something went wrong, please try again.")
        print(e)
        exit(1)


if __name__ == "__main__":
    db_name = "cinemabase.db"
    create_tables(db_name)
    main()
