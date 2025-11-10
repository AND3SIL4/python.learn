# Crea una función que reciba dos cadenas como parámetro (str1, str2)
# e imprima otras dos cadenas como salida (out1, out2).
# - out1 contendrá todos los caracteres presentes en la str1 pero NO
#   estén presentes en str2.
# - out2 contendrá todos los caracteres presentes en la str2 pero NO
#   estén presentes en str1.

# Apply the tdd (test driven design) to solve the problem
import pytest


# Make assertive test
@pytest.mark.parametrize(
    "string1, string2, expected1, expected2",
    [("andres", "felipe", "andrs", "flip"), ("Hola", "aloh", "", "")],
)
def test_return_characters(
    string1: str, string2: str, expected1: str, expected2: str
) -> None:
    response1, response2 = return_characters(string1=string1, string2=string2)
    assert response1 == expected1, "Expected 1 is no valid"
    assert response2 == expected2, "Expected 2 is no valid"


# Make negative test
@pytest.mark.parametrize(
    "string1, string2, type_error, error_message",
    [
        (
            1324,
            "andres",
            TypeError,
            "One or more input strings are not valid, please try again",
        ),
        (
            "felipe",
            2145,
            TypeError,
            "One or more input strings are not valid, please try again",
        ),
    ],
)
def test_error_type(
    string1: str, string2: str, type_error: Exception, error_message: str
) -> None:
    with pytest.raises(type_error, match=error_message):
        return_characters(string1=string1, string2=string2)


# Create main logic
def return_characters(string1, string2) -> tuple[str, str]:
    # Validate if the string are valid
    if not isinstance(string1, str) or not isinstance(string2, str):
        raise TypeError("One or more input strings are not valid, please try again")

    # Validate the strings into both inputs
    # 1. Get the intersection of the strings
    # 1.1 Parse the string lowercase to match the common characters
    # 1.2 Convert the string into a set
    set1 = string1.lower()
    set2 = string2.lower()

    # Crate a tuple for unique common characters
    common_characters = set[str](set1).intersection(set2)

    # 2. Remove the common characters in both sets
    result1 = "".join([ch for ch in set1 if ch not in common_characters])
    result2 = "".join([ch for ch in set2 if ch not in common_characters])

    # 3. Return the result as a tuple
    return result1, result2


print(return_characters(string1="andres", string2="felipe"))
