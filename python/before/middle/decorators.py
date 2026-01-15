import sys
import os


def error_handler(func) -> callable:
    """
    A decorator that handles exceptions in the decorated function and returns a status dictionary.

    This decorator wraps a function to catch any exceptions that occur during its execution.
    On success, it returns a dictionary with `True` and a success message. On failure, it returns
    a dictionary with `False` and an error message containing the exception type, filename, line
    number, and exception message. The decorator traverses the traceback to identify the
    exact line in the decorated function where the exception was raised.

    Args:
        func (callable): The function to be decorated.

    Returns:
        callable: A wrapper function that executes the decorated function and handles exceptions.

    Example:
        >>> @error_handler
        ... def my_function():
        ...     print("Running")
        ...     raise ValueError("Test error")
        ...
        >>> dictionary = my_function()
        >>> print(dictionary)
        Running
        False Error in my_function: ValueError at script.py:4 | Test error
    """

    def wrapper(*args, **kwargs) -> dict[str, any]:
        try:
            func(*args, **kwargs)
            return {
                "status": True,
                "message": f"Function: {func.__name__} executed successfully",
            }
        except Exception as e:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            # Traverse the traceback to find the frame where the exception originated
            tb = exc_tb
            while tb:
                # Check if the current frame is the decorated function
                if tb.tb_frame.f_code.co_name == func.__name__:
                    break
                tb = tb.tb_next
            if tb:
                fname = os.path.split(tb.tb_frame.f_code.co_filename)[1]
                line_no = tb.tb_lineno
            else:
                fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
                line_no = exc_tb.tb_lineno
            error_message = f"Error in {func.__name__}: {exc_type.__name__} at {fname}:{line_no} | {str(e)}"
            # Return a dictionary with status and the error message
            return {
                "status": False,
                "message": error_message,
            }

    # Return the wrapper function
    return wrapper


# This is how the decorator could be is used
@error_handler
def main() -> dict[str, any]:
    print("Hello world")
    raise ValueError("Test error")
    print("Bye world")


# Execute the main function when this file is run
if __name__ == "__main__":
    result: dict = main()
    # Manage the error here, as you need
    if result.get("status", None):
        print("The exception was made successfully")
    else:
        print("There is an error during the execution")
        print(result.get("message", "There is no message"))
