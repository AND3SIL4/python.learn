def exchangeable_value(budget, exchange_rate, spread, denomination):
    # Convert spread to decimal
    spread_decimal = spread / 100

    # Calculate the actual exchange rate including the spread
    actual_exchange_rate = exchange_rate + (exchange_rate * spread_decimal)

    # Calculate the maximum value of the new currency
    exchanged_value = budget / actual_exchange_rate

    # Since the currency denomination is a whole number, we need to divide the exchanged value by the denomination
    # and then take the floor (convert to int) to get the maximum number of whole denominations that can be bought
    max_value = int(exchanged_value * denomination)

    return max_value


print(exchangeable_value(127.25, 1.20, 10, 20))
