# Crea un programa que invierta el orden de una cadena de texto
# sin usar funciones propias del lenguaje que lo hagan de forma automática.
# - Si le pasamos "Hola mundo" nos retornaría "odnum aloH"
import pytest  # type: ignore


@pytest.mark.parametrize("string, expected", [("Hola mundo", "odnum aloH")])
def test_reverse_string(string: str, expected: str) -> None:
    result = reverse_string(string=string)
    assert result == expected, f"The result is not expected for string {string}"


@pytest.mark.parametrize(
    "string, error_type, message",
    [(124, TypeError, "The input should be a valid string"), (None, TypeError, "The input should be a valid string")],
)
def test_negative_reverse_string(string: str, error_type, message: str) -> None:
    with pytest.raises(error_type, match=message):
        reverse_string(string=string)


def reverse_string(string: str) -> str:
    # Validate if there is a valid string passed
    if not isinstance(string, str):
        raise TypeError("The input should be a valid string")

    # Iterate the string
    reversed_list: list[str] = []
    for character in range(len(string) - 1, -1, -1):
        reversed_list.append(string[character])

    return "".join(reversed_list)


STRING = "Hola mundo"
print(reverse_string(string=STRING))
