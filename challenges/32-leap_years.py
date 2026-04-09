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


def get_leap_years(year: int) -> bool:
    # Return the yield iterator with leap years
    while True:
        if (year % 4) == 0 and (year % 100 != 0 or year % 400 != 0):
            yield year
        year += 1


def leap_years(year: int, qty_years: int):
    # Get the iterator leap years to iterate depends on the range
    gen = get_leap_years(year)
    return [next(gen) for _ in range(qty_years)]
