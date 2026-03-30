# Escribe una función que calcule si un número dado es un número de Armstrong
# (o también llamado narcisista).
# Si no conoces qué es un número de Armstrong, debes buscar información
# al respecto.

# Armstrong número: número que es igual a la suma de sus propios digitos
# Cada uno elevado a la potencia del número total de digitos

# Apply the tdd (test driven design) to solve the main problem
import pytest  # type: ignore


# Make assertive tests
@pytest.mark.parametrize(
    "number, expected",
    [(153, True), (12, False), (370, True), (371, True), (407, True)],
)
def test_know_armstrong_number(number: int, expected: bool) -> None:
    assert know_armstrong_number(number=number) == expected, (
        "The expected result is not valid"
    )


# Make negative tests
@pytest.mark.parametrize(
    "number, error_type, expected",
    [
        ("993", TypeError, "The input type is not valid, '993'"),
        (1.23, TypeError, "The input type is not valid, '1.23'"),
    ],
)
def test_wrong_armstrong_number(
    number: int, error_type: Exception, expected: str
) -> None:
    with pytest.raises(error_type, match=expected):
        know_armstrong_number(number=number)


# Make the logic for passing the test
def know_armstrong_number(number) -> bool:
    # 1. Validate if the input type is valid
    if not isinstance(number, int):
        raise TypeError(f"The input type is not valid, '{number}'")

    str_number = str(number)
    digits = len(str_number)  # Calculate the amount of digits to power

    total = 0
    for n in str_number:
        total += int(n) ** digits

    return number == total  # Return the validation


print(know_armstrong_number(153))
