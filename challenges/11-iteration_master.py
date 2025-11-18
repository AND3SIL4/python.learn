# Crea un programa que calcule quien gana más partidas al piedra,
# papel, tijera.
# - El resultado puede ser: "Player 1", "Player 2", "Tie" (empate)
# - La función recibe un listado que contiene pares, representando cada jugada.
# - El par puede contener combinaciones de "R" (piedra), "P" (papel)
#   o "S" (tijera).
# - Ejemplo. Entrada: [("R","S"), ("S","R"), ("P","S")]. Resultado: "Player 2".

# Using tdd (test driven development) to solve the problem
import pytest  # type: ignore
from typing import Literal


# # Make the assertive tests
# @pytest.mark.parametrize(
#     "input, expected", [([("R", "S"), ("S", "R"), ("P", "S")], "Player 2")]
# )
# def test_know_who_wins(
#     input: list[tuple[Literal["P", "S", "R"]]], expected: str
# ) -> None:
#     assert know_who_wins(scores=input) == expected, "The expected value is not valid"


# Make the negative tests
@pytest.mark.parametrize(
    "input_tuple, error_type, expected",
    [
        ([(2, "S"), ("S", "S")], TypeError, "The type of the input is invalid"),
        ([("R", 3), ("S", "S")], TypeError, "The type of the input is invalid"),
        ([("R", "S"), (2, "S")], TypeError, "The type of the input is invalid"),
        ([("R", "S"), ("P", 2)], TypeError, "The type of the input is invalid"),
    ],
)
def test_wrong_type_know_who_wins(
    input_tuple: list[tuple[Literal["P", "S", "R"]]], error_type: Exception, expected: str
) -> None:
    with pytest.raises(error_type, match=expected):
        know_who_wins(scores=input_tuple)


# Make the main logic
def know_who_wins(scores: list[tuple[Literal["P", "R", "S"]]]):
    # 1. Validate the input types 
    for score in scores:
        wrong_types = {tpltype for tpltype in score if not isinstance(tpltype, str)}
        if wrong_types:
            raise TypeError("The type of the input is invalid")



# print(know_who_wins(scores=[("R","S"), ("S","R"), ("P","S")]))
# print(know_who_wins(scores=[(2,"S"), ("S","R"), ("P","S")]))
