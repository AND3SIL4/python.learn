# Crea una función que imprima los 30 próximos años bisiestos
# siguientes a uno dado.
# - Utiliza el menor número de líneas para resolver el ejercicio.
import pytest


@pytest.mark.parametrize(
    "year, amount_dates, expected",
    [
        (2020, 3, [2020, 2024, 2028]),
        (2024, 4, [2024, 2028, 2032, 2036]),
        (2030, 5, [2032, 2036, 2040, 2044, 2048]),
    ],
)
def test_leap_years(year, amount_dates, expected):
    assert leap_years(year, amount_dates) == expected


def leap_years(year: int, amount_dates: int):
    leap_years: list[int] = []
    while len(leap_years) < amount_dates:
        if (year % 4) == 0 and (year % 100 != 0 or year % 400 != 0):
            leap_years.append(year)
        # Increment the year to validate
        year += 1
    # Return the final list of leap years
    return leap_years
