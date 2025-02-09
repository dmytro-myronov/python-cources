import json

def load_books(filename):
    """Loads books from a JSON file."""
    try:
        with open(filename, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_books(filename, books):
    """Saves books to a JSON file."""
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(books, file, ensure_ascii=False, indent=4)

def list_available_books(books):
    """Displays a list of available books."""
    print("Available books:")
    for book in books:
        if book["availability"]:
            print(f"{book['title']} - {book['author']} ({book['year']})")
    print("Not Available books:")
    for book in books:
        if not book["availability"]:
            print(f"{book['title']} - {book['author']} ({book['year']})")

def add_book(filename, title, author, year, available):
    """Adds a new book to the JSON file."""
    books = load_books(filename)
    books.append({"title": title, "author": author, "year": year, "availability": available})
    save_books(filename, books)
    print(f"Book '{title}' added successfully!")


FILENAME = "books.json"
books = load_books(FILENAME)
list_available_books(books)

try :
    # Adding a new book
    new_title = input("Enter the book title: ")
    new_author = input("Enter the book author: ")
    new_year = int(input("Enter the publication year: "))
    new_available = input("Is the book available? (yes/no): ").strip().lower() == "yes"

    add_book(FILENAME, new_title, new_author, new_year, new_available)
except ValueError as e:
    print(f"please enter valid data {e}")
except Exception as e:
    print(f"An error occurred: {e}")


