# Crea una función que ordene y retorne una matriz de números.
# - La función recibirá un listado (por ejemplo [2, 4, 6, 8, 9]) y un parámetro
#   adicional "Asc" o "Desc" para indicar si debe ordenarse de menor a mayor
#   o de mayor a menor.
# - No se pueden utilizar funciones propias del lenguaje que lo resuelvan
#   automáticamente.

# Utilizar TDD (test driven development) to solve the problem
import pytest  # type: ignore
from typing import Literal


# Make the assertive tests
@pytest.mark.parametrize(
    "list_to_be_sorted, order, expected", [([2, 4, 6, 8, 9], "Desc", [9, 8, 6, 4, 2])]
)
def test_sort_list(
    list_to_be_sorted: list[int], order: Literal["Asc", "Desc"], expected
) -> None:
    assert sort_list(list_to_be_sorted=list_to_be_sorted, order=order) == expected


# Make the negative tests
@pytest.mark.parametrize(
    "list_to_be_sorted, order, error_type, expected",
    [
        (
            [2, 4.3, 6, 8, 9.3],
            "Desc",
            TypeError,
            "The input type is not valid, please try again",
        ),
        (
            ["2", 4.3, "6", 8, 9.3],
            "Desc",
            TypeError,
            "The input type is not valid, please try again",
        ),
        (
            [2, 4, 8, 9],
            "Another",
            ValueError,
            "The order argument is not valid",
        ),
    ],
)
def test_negative_sort_list(
    list_to_be_sorted: list[int],
    order: Literal["Asc", "Desc"],
    error_type: Exception,
    expected: str,
) -> None:
    with pytest.raises(error_type, match=expected):
        sort_list(list_to_be_sorted=list_to_be_sorted, order=order)


def sort_list(list_to_be_sorted, order: Literal["Asc", "Desc"]) -> list[int]:
    # Validate if the input are valid
    # Get the data types
    sub_types = set[str](isinstance(i, int) for i in list_to_be_sorted)
    if not all(sub_types):
        raise TypeError("The input type is not valid, please try again")

    n = len(list_to_be_sorted)

    match order:
        case "Asc":
            swapped = False
            for j in range(n):
                for i in range(0, n - j - 1):
                    if list_to_be_sorted[i] > list_to_be_sorted[i + 1]:
                        list_to_be_sorted[i + 1], list_to_be_sorted[i] = (
                            list_to_be_sorted[i],
                            list_to_be_sorted[i + 1],
                        )
                        swapped = True

                if not swapped:
                    break
            return list_to_be_sorted

        case "Desc":
            swapped = False
            for j in range(n):
                for i in range(0, n - j - 1):
                    if list_to_be_sorted[i + 1] > list_to_be_sorted[i]:
                        list_to_be_sorted[i + 1], list_to_be_sorted[i] = (
                            list_to_be_sorted[i],
                            list_to_be_sorted[i + 1],
                        )
                        swapped = True

                if not swapped:
                    break
            return list_to_be_sorted
        case _:
            raise ValueError("The order argument is not valid")


print(sort_list(list_to_be_sorted=[2, 4, 6, 8, 9], order="Desc"))
# print(sort_list(list_to_be_sorted=[140, 56, 2, 1], order="Asc"))
# print(sort_list(list_to_be_sorted=[2, 4.3, 6, 8, 9.3], order="Desc"))
