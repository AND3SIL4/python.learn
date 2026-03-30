# Crea una función que reciba días, horas, minutos y segundos (como enteros)
# y retorne su resultado en milisegundos.

# Apply tdd (test driven design) for solving the problem
import pytest  # type: ignore


# Make the assertive tests
@pytest.mark.parametrize(
    "days, hours, minutes, seconds, expected",
    [
        (3, 4, 10, 7, 274207000),
        (2, 6, 15, 30, 195330000),
        (1, 12, 45, 5, 132305000),
        (0, 5, 20, 50, 19250000),
        (0, 0, 0, 0, 0),
    ],
)
def test_time_parser(
    days: int, hours: int, minutes: int, seconds, expected: int
) -> None:
    assert (
        time_parser(days=days, hours=hours, minutes=minutes, seconds=seconds)
        == expected
    ), "Error getting the expected value"


# Make the negative tests
@pytest.mark.parametrize(
    "days, hours, minutes, seconds, error_type, expected",
    [
        ("Hola", 5, 3, 1, TypeError, "The input type 'days' is not valid"),
        (1, "Hola", 4, 5, TypeError, "The input type 'hours' is not valid"),
        (1, 2, "Hola", 5, TypeError, "The input type 'minutes' is not valid"),
        (1, 2, 4, "Hola", TypeError, "The input type 'seconds' is not valid"),
    ],
)
def test_time_parser_error_type(
    days: int,
    hours: int,
    minutes: int,
    seconds: int,
    error_type: Exception,
    expected: int,
) -> None:
    with pytest.raises(error_type, match=expected):
        time_parser(days=days, hours=hours, minutes=minutes, seconds=seconds)


# Make the negative tests
@pytest.mark.parametrize(
    "days, hours, minutes, seconds, error_type, expected",
    [
        (None, 5, 3, 1, ValueError, "Missing 'days' should be 0 insted of None"),
        (1, None, 4, 5, ValueError, "Missing 'hours' should be 0 insted of None"),
        (1, 2, None, 5, ValueError, "Missing 'minutes' should be 0 insted of None"),
        (1, 2, 4, None, ValueError, "Missing 'seconds' should be 0 insted of None"),
    ],
)
def test_time_parser_missing_args(
    days: int,
    hours: int,
    minutes: int,
    seconds: int,
    error_type: Exception,
    expected: int,
) -> None:
    with pytest.raises(error_type, match=expected):
        time_parser(days=days, hours=hours, minutes=minutes, seconds=seconds)


# Make the main logic
def time_parser(days, hours, minutes, seconds) -> int:
    for name, value in locals().items():
        # 1. Validate if there is a param missing
        if value is None:
            raise ValueError(f"Missing '{name}' should be 0 insted of None")
        # 2. Validate the type of the params
        if not isinstance(value, int):
            raise TypeError(f"The input type '{name}' is not valid")

    # Apply the main logic for passing the tests
    # 2. Convert input time to seconds
    s_in_days = days * 24 * 3600
    s_in_hours = hours * 3600
    s_in_minutes = minutes * 60
    # Calculate the total seconds
    total_seconds = s_in_days + s_in_hours + s_in_minutes + seconds
    # Return the total milli seconds
    return total_seconds * 1000
