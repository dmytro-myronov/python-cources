"""
Simple calculator that evaluates user input expressions.
Handles various exceptions to provide user-friendly error messages.
"""

class UnknownOperationError(Exception):
    """Exception raised for unknown operations."""
    pass


def init_calc():
    """
    Starts a loop to take user input for calculations.
    Evaluates expressions and handles errors gracefully.
    Type 'end' to exit the calculator.
    """
    while True:
        eval_value = input("please enter command to calc: ")
        try:
            if eval_value == "end":
                print("exit!")
                break
            res = eval(eval_value)
            print(res)
        except ZeroDivisionError:
            print("Zero division")
        except ValueError:
            print("please enter correct value")
        except NameError:
            print("please add correct num expression")
        except SyntaxError:
            print("please add correct syntax")
        except MemoryError:
            print("Memory error! Not enough memory")
        except Exception as e:
            print(f"something went wrong {e}")


init_calc()
