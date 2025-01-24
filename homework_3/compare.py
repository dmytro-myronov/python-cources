class Person:
    """
    A class to represent a person with a name and age.

    Attributes:
        name (str): The name of the person.
        age (int): The age of the person.
    """

    def __init__(self, name, age):
        """
        Initializes a new person with the given name and age.

        Args:
            name (str): The name of the person.
            age (int): The age of the person.
        """
        self.name = name
        self.age = age

    def __lt__(self, other):
        """
        Compares the age of the current person with another person.

        Args:
            other (Person): Another person object to compare with.

        Returns:
            bool: True if the current person's age is less than the other person's age.
        """
        return self.age < other.age

    def __eq__(self, other):
        """
        Compares the age of the current person with another person.

        Args:
            other (Person): Another person object to compare with.

        Returns:
            bool: True if the current person's age is equal to the other person's age.
        """
        return self.age == other.age

    def __gt__(self, other):
        """
        Compares the age of the current person with another person.

        Args:
            other (Person): Another person object to compare with.

        Returns:
            bool: True if the current person's age is greater than the other person's age.
        """
        return self.age > other.age

    def __repr__(self):
        """
        Returns a string representation of the person object.

        Returns:
            str: A string representation of the person with their name and age.
        """
        return f"Person(name={self.name}, age={self.age})"



# Creating a list of Person objects
people = [
    Person("Alice", 30),
    Person("Bob", 25),
    Person("Charlie", 35),
    Person("David", 28)
]

# Sorting the list of people by age (using the __lt__ method)
sorted_people = sorted(people)

# Printing the sorted list
for person in sorted_people:
    print(person)
