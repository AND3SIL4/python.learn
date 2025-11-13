# Crea una función que reciba un String de cualquier tipo y se encargue de
# poner en mayúscula la primera letra de cada palabra.
# - No se pueden utilizar operaciones del lenguaje que
#   lo resuelvan directamente.


# Apply tdd (test driven design) for solving the problem
import pytest


# Create the assertive tests
@pytest.mark.parametrize(
    "string, expected",
    [
        ("andres felipe silva", "Andres Felipe Silva"),
        ("Andres Silva", "Andres Silva"),
        ("andres", "Andres"),
        ("anDRes", "Andres"),
    ],
)
def test_capitalize_string(string: str, expected: str) -> None:
    assert capitalize_string(string=string) == expected, (
        "The expected output is not valid"
    )


# Create the negative tests
@pytest.mark.parametrize(
    "string, error_type, expected",
    [
        (1344, TypeError, "The input type is not valid"),
        ("", ValueError, "The input string is empty"),
    ],
)
def test_wrong_capitalize_string(
    string: str, error_type: Exception, expected: str
) -> None:
    with pytest.raises(error_type, match=expected):
        capitalize_string(string=string)


# Make de main logic for passing the tests
def capitalize_string(string) -> str:
    # 1. Validate if the input type is correct
    if not isinstance(string, str):
        raise TypeError("The input type is not valid")

    # 2. Validate if the string is empty
    if not string:
        raise ValueError("The input string is empty")

    # 3. Make the logic for parsing to capitalize the string
    # 3.1 Split the string to complete words as needed
    words = string.split(" ")

    # 3.2 Iterate over all words and validate the firts character of the words
    for i, word in enumerate[str](words):
        # Take the first letter of the word
        if not word[0].isupper():
            # Take teh first word and apply the capitalization
            words[i] = word[0].upper() + word[1:].lower()
    return " ".join(words)


print(capitalize_string("andres felipe silva"))
print(capitalize_string("Andres"))
