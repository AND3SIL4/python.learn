# Crea una función que reciba un texto y muestre cada palabra en una línea,
# formando un marco rectangular de asteriscos.
# - ¿Qué te parece el reto? Se vería así:
import pytest  # type: ignore

output = """\
**********
* ¿Qué   *
* te     *
* parece *
* el     *
* reto?  *
**********"""


@pytest.mark.parametrize("income, output", [("¿Qué te parece el reto?", output)])
def test_wrap_text(income: str, output: str):
    assert wrap_string(income) == output, "The output expecting is not valid"


def wrap_string(string: str):
    words: list[str] = string.split()
    max_word_length = max(len(w) for w in words)

    # Sum 4 characters to include the edges and the spaces
    edge = "*" * int(max_word_length + 4)
    final_string = [edge]
    for w in words:
        final_string.append(f"* {w.ljust(max_word_length)} *")
    final_string.append(edge)
    return "\n".join(final_string)


print(wrap_string("¿Qué te parece el reto?"))
