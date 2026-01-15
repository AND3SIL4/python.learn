#  Escribe un programa que muestre por consola (con un print) los
#  números de 1 a 100 (ambos incluidos y con un salto de línea entre
#  cada impresión), sustituyendo los siguientes:
#  - Múltiplos de 3 por la palabra "fizz".
#  - Múltiplos de 5 por la palabra "buzz".
#  - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".


# Generate the test before make the main logic
def test_fizz_buzz() -> None:
    """Unit test for fizz buzz generation"""
    # Test the normal cases
    normal_cases = [1, 2, 7, 11, 13]
    for n in normal_cases:
        result = list[int | str](fizz_buzz(range_generator=range(n, n + 1)))
        assert result[0] == n, f"Falló para número {n}"

    # Test the fizz cases
    fizz_cases = [3, 6, 9]
    for n in fizz_cases:
        result = list[int | str](fizz_buzz(range_generator=range(n, n + 1)))
        assert result[0] == "Fizz", f"Falló el Fizz para el número {n}"

    # Test Buzz cases
    buzz_cases = [5, 10, 20]
    for n in buzz_cases:
        result = list[int | str](fizz_buzz(range_generator=range(n, n + 1)))
        assert result[0] == "Buzz", f"Falló el Buzz para el número {n}"

    # Test Fizz Buzz cases
    fizz_buzz_cases = [15, 30, 45]
    for n in fizz_buzz_cases:
        result = list[int | str](fizz_buzz(range_generator=range(n, n + 1)))
        assert result[0] == "Fizz Buzz", f"Falló el Fizz Buzz para el número {n}"


# Algorithm solution
# 1. Print the entire range of numbers
# 2. Validate the both multiples and return the word "Fizz Buzz"
# 3. Replace the number with the word "fizz" applying the validation
# 4. Replace the other number with the word "buzz" applying the validation
# 5. The numbers which does not match, only will be printed normally


def fizz_buzz(range_generator: range) -> None:
    for i in range_generator:
        # Multiples of numbers 3 and 5
        # We can use the 15 multiple to avoid evaluate twice
        # if i % 3 == 0 and i % 5 == 0:
        if i % 15 == 0:
            yield ("Fizz Buzz")
        # Multiples of numbers 3
        elif i % 3 == 0:
            yield ("Fizz")
        # Multiples of 5
        elif i % 5 == 0:
            yield ("Buzz")
        else:
            yield (i)


# Call the main function
if __name__ == "__main__":
    for value in fizz_buzz(range_generator=range(1, 101)):
        print(value)
