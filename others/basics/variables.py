## Variables are written by snack_case
def variables():
    variable = 1
    print(variable)


variables()


## Constant are written by SCREAMING_SNAKE_CASE
def constants():
    CONSTANTE = 1
    CONSTANTE = 3
    print(CONSTANTE)


constants()


## Docstring are calling fro show the (""" """) notation for instance
## Key word = .__doc___ after the param or function
def doc_strings(number):
    """
    Raise a double of the number inputted
    :param number: int the base number
    :return: int the double of the number
    """

    return number * 2


print(doc_strings.__doc__)
