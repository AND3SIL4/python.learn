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
def wrong_capitalize_string(string: str, error_type: Exception, expected: str) -> None:
    with pytest.raises(error_type, match=expected):
        capitalize_string(string=string)


# Make de main logic for passing the tests
def capitalize_string(string) -> str: ...
