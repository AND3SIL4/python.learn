# Crea un programa que se encargue de transformar un número
# decimal a binario sin utilizar funciones propias del lenguaje que lo hagan directamente.

# * Apply TDD approach for solving the challenge
import pytest  # type: ignore
from typing import Any


# Using the assert testing
@pytest.mark.parametrize("decimal, expected", [(1, "1"), (124, "1111100")])
def test_decimal_to_binay(decimal: int, expected: str) -> None:
    assert decimal_to_binary(decimal=decimal) == expected, (
        f"The decimal {decimal} is not converted to binary correctly"
    )


# Using the negative testing
@pytest.mark.parametrize(
    "decimal, error_type, expected",
    [
        ("Test", TypeError, "The input 'Test' should be a valid decimal"),
        (1.3, TypeError, "The input '1.3' should be a valid decimal"),
    ],
)
def test_error_negative(decimal, error_type, expected) -> None:
    with pytest.raises(error_type, match=expected):
        decimal_to_binary(decimal=decimal)


def decimal_to_binary(decimal: int | Any) -> str:
    # Validate if there is a valid decimal
    if not isinstance(decimal, int):
        raise TypeError(f"The input '{decimal}' should be a valid decimal")

    # Create a list to store the binary convination
    binary_conbination: list[str] = []
    while decimal != 0:
        decimal, remainder = divmod(decimal, 2)
        # Add a result to final binary convertion
        binary_conbination.append(str(remainder))

    # Reverse the list to be returned
    reversed_list: list[str] = binary_conbination[::-1]
    # Return the result as string reversing the binary
    return "".join(reversed_list)


print(decimal_to_binary(decimal=124))
