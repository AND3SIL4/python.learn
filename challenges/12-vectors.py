# Crea un programa que determine si dos vectores son ortogonales.
# - Los dos array deben tener la misma longitud.
# - Cada vector se podría representar como un array. Ejemplo: [1, -2]

# Using tdd (test driven desing) to solve the problem
import pytest  # type: ignore


# Make possitive tests
@pytest.mark.parametrize("vector1, vector2, expected", [()])
def test_is_orthogonal_vector(
    vector1: list[int], vector2: list[int], expected: bool
) -> None:
    assert is_orthogonal_vector(vecto1=vector1, vector2=vector2) == expected, (
        "The expected and return value does not match"
    )


# Make negative tests
@pytest.mark.parametrize("vector1, vector2, error_type, expected", [()])
def test_error_is_orthogonal_vector(
    vector1: list[int], vector2: list[int], error_type: Exception, expected: str
) -> None:
    with pytest.raises(error_type, match=expected):
        is_orthogonal_vector(vecto1=vector1, vector2=vector2)


# Apply the main logic to know if the vectors are orthogonal
def is_orthogonal_vector(vecto1: list[int], vector2: list[int]) -> None: ...
