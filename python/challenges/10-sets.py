# Crea una función que reciba dos array, un booleano y retorne un array.
# - Si el booleano es verdadero buscará y retornará los elementos comunes
#   de los dos array.
# - Si el booleano es falso buscará y retornará los elementos no comunes
#   de los dos array.
# - No se pueden utilizar operaciones del lenguaje que
#   lo resuelvan directamente.


# Using tdd (test driven design) for solving the main problem
import pytest  # type: ignore


# # Make the assertive tests
@pytest.mark.parametrize(
    "arr1, arr2, common, expected",
    [
        ([1, 2, 3, 4], [34, 1, 2, 8], True, [1, 2]),
        ([1, 2, 3, 4], [34, 1, 2, 8], False, [3, 4, 8, 34]),
        (
            ["hola", "andres", "Felipe"],
            ["andres", "Felipe"],
            True,
            ["Felipe", "andres"],
        ),
        (
            ["hola", "andres", "Felipe"],
            ["Andres", "Felipe"],
            False,
            ["Andres", "andres", "hola"],
        ),
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
        # (None, [12], True, TypeError, "The input type is not valid"),
        # (["sfasd"], None, True, TypeError, "The input type is not valid"),
        (["hola"], [12], True, TypeError, "Inputs type does not match"),
        ([24], ["hola"], True, TypeError, "Inputs type does not match"),
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
def know_sets(arr1, arr2, common: bool = True) -> set[int | str]:
    # 1. Make type validations, check is a list is passed
    if not isinstance(arr1, list) or not isinstance(arr2, list):
        raise TypeError("The input type is not valid")

    # 1.1 Get the types of each array passed
    types_arr1 = {type(e) for e in arr1}
    types_arr2 = {type(e) for e in arr2}

    # 1.2. Validate if the types match
    if types_arr1 != types_arr2:
        raise TypeError("Inputs type does not match")

    # 2. Apply the main logic
    result = []
    if common:
        result = set[int | str](arr1).intersection(arr2)
    else:
        result = set[int | str](arr1).difference(arr2)
        result = result.union(set[int | str](arr2).difference(arr1))
    return sorted(list[str | int](result))


# know_sets(None, [12], True)
# know_sets(["sfasd"], None, True)
# print(know_sets([2, 2, 3], [1, 2], True))
# print(know_sets([2, 2, 3], [1, 2], False))
# know_sets(["hola"], [12], True)
# know_sets([24], ["hola"], True)
print(know_sets(["hola", "andres", "Felipe"], ["Andres", "Felipe"], False))
