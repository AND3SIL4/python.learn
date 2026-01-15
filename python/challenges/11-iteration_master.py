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


# Make the assertive tests
@pytest.mark.parametrize(
    "input, expected", [([("R", "S"), ("S", "R"), ("P", "S")], "Player 2")]
)
def test_know_who_wins(
    input: list[tuple[Literal["P", "S", "R"]]], expected: str
) -> None:
    assert know_who_wins(scores=input) == expected, "The expected value is not valid"


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
    input_tuple: list[tuple[Literal["P", "S", "R"]]],
    error_type: Exception,
    expected: str,
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

    # 2. Apply the main logic
    score_player1 = 0
    score_player2 = 0
    for score in scores:
        # Extrar the values from the tuple
        player1, player2 = score
        if compare_options(option1=player1, option2=player2) == player1:
            score_player1 += 1
        elif compare_options(option1=player1, option2=player2) == player2:
            score_player2 += 2

    return "Player 1" if score_player1 > score_player2 else "Player 2"


def compare_options(option1: str, option2: str) -> str:
    # Improved logic using a rule dictionary for Rock-Paper-Scissors
    # Returns the winning option, or None if it's a tie
    rules = {
        ("R", "S"): "R",
        ("S", "R"): "R",
        ("S", "P"): "S",
        ("P", "S"): "S",
        ("P", "R"): "P",
        ("R", "P"): "P",
    }
    if option1 == option2:
        return None  # It's a tie
    return rules.get((option1, option2))


print(know_who_wins(scores=[("R", "S"), ("S", "R"), ("P", "S")]))
# print(know_who_wins(scores=[(2,"S"), ("S","R"), ("P","S")]))
