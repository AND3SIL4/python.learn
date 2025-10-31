# Crea una única función (importante que sólo sea una) que sea capaz
# de calcular y retornar el área de un polígono.
# - La función recibirá por parámetro sólo UN polígono a la vez.
# - Los polígonos soportados serán Triángulo, Cuadrado y Rectángulo.
# - Imprime el cálculo del área de un polígono de cada tipo.
import pytest  # type: ignore
from typing import Literal


@pytest.mark.parametrize(
    "polygon, base, height, expected",
    [("triangle", 3, 3, 4.5), ("square", 2, 2, 4), ("rectangle", 5, 5, 25)],
)
def test_calculate_area(polygon, base, height, expected) -> None:
    # Test a triangle area, rectangle area and sqaure area
    result = calculate_area(polygon=polygon, base=base, height=height)
    assert result == expected, (
        f"The area calculated is not valid for the polygon {polygon}"
    )


# Make a negative test
def test_invalid_area():
    with pytest.raises(
        ValueError, match="The current polygon passed another is not valid"
    ):
        calculate_area("another", 2, 2)


def calculate_area(
    polygon: Literal["triangle", "square", "rectangle"],
    base: int | float,
    height: int | float,
) -> int | float:
    # Validate if there is a valid polygon passed
    valid_polygons = ["triangle", "square", "rectangle"]
    if polygon not in valid_polygons:
        raise ValueError(f"The current polygon passed {polygon} is not valid")
    if polygon == "triangle":
        return (base * height) / 2
    else:
        return base * height
