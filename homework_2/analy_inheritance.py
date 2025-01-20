import inspect

def analyze_inheritance(obj):
    """
    Analyzes the inheritance hierarchy of the given class and prints the parent classes.

    Args:
        obj (type): The class to analyze.
    """
    print(f"class {obj.__name__} has next parents:")
    # Get the method resolution order (MRO) for the class
    for class_type in inspect.getmro(obj):
        # Skip the class itself to only print its parents
        if class_type.__name__ != obj.__name__:
            print(f"Parent class name:  {class_type.__name__}")

class Animals:
    """
    Base class representing animals.
    """
    pass

class Cats(Animals):
    """
    Class representing cats, which inherits from Animals.
    """
    def parent_method(self):
        """
        A method that would be inherited by subclasses.
        """
        pass

class Tiger(Cats):
    """
    Class representing tigers, which inherit from Cats.
    """
    def child_method(self):
        """
        A method specific to the Tiger class.
        """
        pass

# Analyze the inheritance hierarchy of the Tiger class
analyze_inheritance(Tiger)
