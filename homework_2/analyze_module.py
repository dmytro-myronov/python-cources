import importlib

module_name = input("Enter the module name: ")

try:
    # Dynamically import the module
    module = importlib.import_module(module_name)

    # Get a list of methods in the module
    methods = [method for method in dir(module) if not method.startswith("__")]

    print(f"Methods in the {module_name} module:")
    print(methods)
except ModuleNotFoundError:
    print(f"The module '{module_name}' was not found.")
except Exception as e:
    print(f"An error occurred: {e}")
