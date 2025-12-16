# Crea un programa que determine si dos vectores son ortogonales.
# - Los dos array deben tener la misma longitud.
# - Cada vector se podría representar como un array. Ejemplo: [1, -2]
# - The vectors must to have a length of 2

"""
For knowing if the vector is orthogonal we have to use the following

- If the product point between two vectors are equal to 0, that means
two vectors are orthogonal
"""

# Using tdd (test driven desing) to solve the problem
import pytest  # type: ignore


# Make possitive tests
@pytest.mark.parametrize(
    "vector1, vector2, expected",
    [
        ([2, 1], [-1, 2], True),
        ([1, 1], [1, -1], True),
        ([2, 3], [3, -2], True),
        ([1, 2], [3, 1], False),
    ],
)
def test_is_orthogonal_vector(
    vector1: list[int], vector2: list[int], expected: bool
) -> None:
    assert is_orthogonal_vector(vecto1=vector1, vector2=vector2) == expected, (
        "The expected and return value does not match"
    )


# Make negative tests
@pytest.mark.parametrize(
    "vector1, vector2, error_type, expected",
    [
        ([1, 2, 3], [1, 2], ValueError, "The length of the vectors are not valid"),
        ([1, 2], [1, 2, 4], ValueError, "The length of the vectors are not valid"),
        (["1", 2], [1, 2], TypeError, "One vector type is not valid"),
        ([1, 2], [1, "4"], TypeError, "One vector type is not valid"),
    ],
)
def test_error_is_orthogonal_vector(
    vector1: list[int], vector2: list[int], error_type: Exception, expected: str
) -> None:
    with pytest.raises(error_type, match=expected):
        is_orthogonal_vector(vecto1=vector1, vector2=vector2)


# Apply the main logic to know if the vectors are orthogonal
def is_orthogonal_vector(vecto1: list[int], vector2: list[int]) -> None: ...
