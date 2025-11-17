# Crea una función que reciba dos array, un booleano y retorne un array.
# - Si el booleano es verdadero buscará y retornará los elementos comunes
#   de los dos array.
# - Si el booleano es falso buscará y retornará los elementos no comunes
#   de los dos array.
# - No se pueden utilizar operaciones del lenguaje que
#   lo resuelvan directamente.


# Using tdd (test driven design) for solving the main problem
from re import U
import pytest  # type: ignore
from typing import Any


# Make the assertive tests
@pytest.mark.parametrize(
    "arr1, arr2, common, expected",
    [
        ([1, 2, 3, 4], [34, 1, 2, 8], True, [1, 2]),
        ([1, 2, 3, 4], [34, 1, 2, 8], False, [1, 2]),
        (["hola", "andres", "Felipe"], ["Andres", "Felipe"], True, ["andres, felipe"]),
        (["hola", "andres", "Felipe"], ["Andres", "Felipe"], False, ["hola"]),
    ],
)
def test_know_sets(
    arr1: list[int | str],
    arr2: list[int | str],
    common: bool,
    expected: list[int | str],
) -> None:
    assert know_sets(arr1=arr1, arr2=arr2, common=common) == expected, (
        "The expected value is not valid"
    )


# Make the negative tests
@pytest.mark.parametrize(
    "arr1, arr2, common, error_type, expected",
    [
        (["hola"], [12], True, TypeError, "The input type is not valid"),
        ([24], ["hola"], True, TypeError, "The input type is not valid"),
    ],
)
def test_error_type(
    arr1: list[int | str],
    arr2: list[int, str],
    common: bool,
    error_type: Exception,
    expected: str,
) -> None:
    with pytest.raises(error_type, match=expected):
        know_sets(arr1=arr1, arr2=arr2, common=common)


# Make the main logic for passing all tests
def know_sets(arr1, arr2, common: bool) -> set:...
