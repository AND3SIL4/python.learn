# Escribe una función que calcule y retorne el factorial de un número dado
# de forma recursiva.

# To solve the problem we'll use the tdd (test driven design)
import pytest  # type: ignore


# 1. Apply the assertive tests
@pytest.mark.parametrize("number, expected", [(3, 6), (2, 2), (6, 720), (1, 1)])
def test_calculate_factorial(number: int, expected: int) -> None:
    assert calculate_factorial(number=number) == expected, "The value is not expected"


# 2. Make the negative tests
@pytest.mark.parametrize(
    "number, error_type, expected",
    [
        ("hola", TypeError, "The type of the input is not valid"),
        (1.3, TypeError, "The type of the input is not valid"),
    ],
)
def test_wrong_calculate_factorial(
    number, error_type: Exception, expected: str
) -> None:
    with pytest.raises(error_type, match=expected):
        calculate_factorial(number=number)


# 3. Consolidate the main logic in order to supply the tests created
def calculate_factorial(number) -> int:
    # 1. Validate if there is a valid number
    if not isinstance(number, int):
        raise TypeError("The type of the input is not valid")

    if number == 1:
        return 1

    return number * calculate_factorial(number - 1)


print(calculate_factorial(number=6))
