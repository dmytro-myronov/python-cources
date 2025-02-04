
class InsufficientResourcesException(Exception):
    def __init__(self, required_resource: str, required_amount: float, current_amount: float):
        self.required_resource = required_resource
        self.required_amount = required_amount
        self.current_amount = current_amount
        super().__init__(self._generate_message())

    def _generate_message(self) -> str:
        return (f"Insufficient resource '{self.required_resource}': "
                f"required {self.required_amount}, but only {self.current_amount} available.")

# Example usage:
def perform_action(resource: str, required: float, available: float):
    if available < required:
        raise InsufficientResourcesException(resource, required, available)
    print("Action performed successfully!")

# Test exception
try:
    perform_action("gold", 100, 75)
except InsufficientResourcesException as e:
    print(e)