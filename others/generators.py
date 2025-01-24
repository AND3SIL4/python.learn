from typing import Generator
# def multiples3(limit: int) -> list[int]:
# num = 3
# result = []
# while num < limit:
# result.append(num)
# num += 3

# return result

# print(multiples3(10))

# def multiples3(limit: int) -> list[int]:
# num = 3
# while num < limit:
# yield num
# num += 3

# result = multiples3(20)
# print(next(result))
# print(next(result))

# Create a function that show the multiples of 4 into a specific limit
# def multiples4(limit: int) -> list[int]:
# num = 4
# result: list[int] = []
# while num < limit:
# result.append(num)
# num += 4

# return result

# limit = int(input("Type a number: "))
# print(multiples4(limit))


# def multiples4(limit: int) -> Generator[int, None, None]:
# num = 4
# while num < limit:
# yield num
# num += 4


# limit = int(input("Type a number: "))
# gen = multiples4(limit)
# for g in gen:
# print(g)

# Create a function that show the numbers that ends with 3
# from 1 to the limit gave by the user
# def show_numbers(limit: int) -> list[int]:
# result = [number for number in range(limit) if number % 10 == 3]

# return result

# limit = int(input("Type a number: "))
# print(show_numbers(limit))

# def show_numbers(limit: int) -> list[int]:
# for number in range(limit):
# if number % 10 == 3:
# yield number


# limit = int(input("Type a number: "))
# for r in show_numbers(limit):
# print(r)

# Create a function that returns the numbers
# when the digit 1 and digit 2 sum 4
# def digits(limit: int) -> list[int]:
# return [
# number
# for number in range(limit)
# if (number // 10) % 10 + number % 10 == 4
# ]


# limit = int(input("Type a number: "))
# print(digits(limit))

# def digits(limit: int) -> Generator[int, None, None]:
# for number in range(limit):
# one = (number // 10) % 10
# two = number % 10

# if one + two == 4:
# yield number


# limit = int(input("Type a number: "))
# for d in digits(limit):
# print(d)

# Create a function that show the numbers with the same two last digits
# def same(limit: int) -> list[int]:
# return [
# number
# for number in range(limit)
# if (number // 10) % 10 == number % 10
# ]


# limit = int(input("Type a number: "))
# print(same(limit))


# def same(limit: int) -> Generator[int, None, None]:
# for number in range(limit):
# if (number // 10) % 10 == number % 10:
# yield number


# limit = int(input("Type a number: "))
# for s in same(limit):
# print(s)

# Create a function that the last 3 numbers are equals to 8
# def last_3(limit: int) -> list[int]:
# return [
# number
# for number in range(limit)
# if (number // 100) % 10 + (number // 10) % 10 + number % 10 == 8
# ]


# limit = int(input("Type a number: "))
# print(last_3())


# def last_3(limit: int) -> list[int]:
# for number in range(limit):
# if (number // 100) % 10 + (number // 10) % 10 + number % 10 == 8:
# yield number


# limit = int(input("Type a number: "))
# for li in last_3(limit):
# print(li)

# Create a function that show the number with 2 digits and
# the number should be odd number
# def odd() -> list[int]:
# return [
# number
# for number in range(10, 100)
# if not number % 2 == 0
# ]


# print(odd())


# def odd() -> list[int]:
# for number in range(10, 100):
# if not number % 2 == 0:
# yield number


# for o in odd():
# print(o)

# Create a function that show the number
# when its two last numbers are multiples
# def multipes(limit: int) -> list[int]:
# resul: list[int] = []
# for number in range(limit):
# num1 = (number // 10) % 10
# num2 = number % 10

# if num1 == 0 or num2 == 0:
# continue

# if (num1 % num2 == 0) or (num2 % num1 == 0):
# resul.append(number)
# return resul


# limit = int(input("Type a number: "))
# print(multipes(limit))


# def multipes(limit: int) -> list[int]:
# for number in range(limit):
# num1 = (number // 10) % 10
# num2 = number % 10

# if num1 == 0 or num2 == 0:
# continue

# if (num1 % num2 == 0) or (num2 % num1 == 0):
# yield number


# limit = int(input("Type a number: "))
# for m in multipes(limit):
# print(m)

# Create a function that shows the first number gave by the user
# def first(num: int, limit: int) -> list[int]:
# result: list[int] = []
# for number in range(limit):
# if str(number).startswith(str(num)):
# result.append(number)

# return result


# num = int(input("Type the number: "))
# limit = int(input("Type the limit: "))
# print(first(num, limit))


# def first(num: int, limit: int) -> list[int]:
# for number in range(limit):
# if str(number).startswith(str(num)):
# yield number


# num = int(input("Type the number: "))
# limit = int(input("Type the limit: "))
# for f in first(num, limit):
# print(f)

# Create a function that show the first and last number when are equals
# def first_last(limit: int) -> list[int]:
# result: list[int] = []
# for number in range(limit):
# first = number
# while first > 10:
# first //= 10

# if first == number % 10:
# result.append(number)

# return result


# limit = int(input("Type the limit: "))
# print(first_last(limit))


# def first_last(limit: int) -> list[int]:
# for number in range(limit):
# first = number
# while first > 10:
# first //= 10

# if first == number % 10:
# yield number


# limit = int(input("Type the limit: "))
# for f in first_last(limit):
# print(f)

# Create a function that show the numbers with
# The firts and last digit are multiples
# def multiples(limit: int) -> list[int]:
# result: list[int] = []
# for number in range(limit):
# aux = number
# while aux > 10:
# aux //= 10

# num = number % 10
# if aux == 0 or num == 0:
# continue

# if (aux % num == 0) or (num % aux == 0):
# result.append(number)

# return result


# limit = int(input("Type a number: "))
# print(multiples(limit))


def multiples(limit: int) -> Generator[int, None, None]:
    for number in range(limit):
        aux = number
        while aux > 10:
            aux //= 10

        num = number % 10
        if aux == 0 or num == 0:
            continue

        if (aux % num == 0) or (num % aux == 0):
            yield number


limit = int(input("Type a number: "))
for m in multiples(limit):
    print(m)
