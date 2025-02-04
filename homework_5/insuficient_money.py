class TransactionType:
    """
    Enum-like class representing different types of financial transactions.
    """
    PURCHASE = "purchase"
    SELL = "sell"
    TRANSFER = "transfer"
    DEPOSIT = "deposit"
    WITHDRAW = "withdraw"


class InsufficientFundsException(Exception):
    """
    Exception raised when an account has insufficient funds for a transaction.

    Attributes:
        required_amount (float): The amount required to complete the transaction.
        current_amount (float): The available amount in the account.
        currency (str): The currency type of the transaction.
        transaction_type (str): The type of transaction attempted.
    """

    def __init__(self, required_amount: float, current_amount: float, currency: str, transaction_type: str):
        self.required_amount = required_amount
        self.current_amount = current_amount
        self.currency = currency
        self.transaction_type = transaction_type
        super().__init__(self._generate_message())

    def _generate_message(self) -> str:
        """
        Generates a descriptive error message for the exception.

        Returns:
            str: The formatted error message.
        """
        return (f"Insufficient funds: Required {self.required_amount} {self.currency}, "
                f"but only {self.current_amount} available. Transaction type: {self.transaction_type}.")


def perform_action(required: float, available: float, currency: str, transaction_type: str):
    """
    Attempts to perform a financial transaction, raising an exception if funds are insufficient.

    Args:
        required (float): The amount required for the transaction.
        available (float): The currently available amount.
        currency (str): The currency of the transaction.
        transaction_type (str): The type of transaction.

    Raises:
        InsufficientFundsException: If available funds are less than the required amount.
    """
    if available < required:
        raise InsufficientFundsException(required, available, currency, transaction_type)
    print(f"Transaction successful! {currency} {required} {transaction_type} ")


# Example usage and exception handling
try:
    perform_action(100, 75, "USD", TransactionType.PURCHASE)
except InsufficientFundsException as e:
    print(e)
except Exception as e:
    print("Something went wrong. try again later")

try:
    perform_action(60, 75, "EUR", TransactionType.TRANSFER)
except InsufficientFundsException as e:
    print(e)
except Exception as e:
    print("Something went wrong. try again later")