# In this document there are some examples of working with exceptions
try:
    # Try to raise a custom exception
    # We can add a text for the exception
    raise Exception("Exception example")

    num1: int = int(input("Type the number 1:"))
    num2: int = int(input("Type the number 2:"))
    result: int = num1 / num2
    print("The result is:", result)
except ValueError:  # This will be execute if there is an value error
    print("The is a value error, plz try again")
except ZeroDivisionError:  # Execute if the user try to divide by zero
    print("You can't divide by zero IDIOT!")
except Exception as e:  # If any other exceptio ocurred
    print(e, type(e))
    # We can add notes for being more specific with exception caught
    e.add_note("This is the note")
    print("Notes:", e.__notes__)
else:  # If the Try block has succeed in its execution
    print("If the try block has been correct I will be execute")
finally:  # Always execute
    print("I will execute always")
