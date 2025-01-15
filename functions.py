# function that takes a string list as a parameter and return the sum of the total letter in each string
def total_letters(lista: list) -> int:
    total = 0
    for word in lista:
        total += len(word)

    return total

# lista = ["Andres", "Felipe", "Silva"]
# print(total_letters(lista))

# Create a function that takes two integers and return the bigger number


def bigger_number(num1: int, num2: int) -> int:
    return num1 if num1 > num2 else num2


# num1 = int(input("Type a number: "))
# num2 = int(input("Type a number: "))
# print(bigger_number(num1, num2))

# Create a function that show a multiplication table depends on the number passed
def multiplication_table(number: int) -> str:
    for i in range(10):
        print(f"{number} * {i} = {number * i}")


# number = int(input("Type a number to show the multiplication table: "))
# multiplication_table(number)

# Create a function to know if the number passed ends with 4
def know_number(number: int) -> bool:
    return abs(number) % 10 == 4

# number = int(input("Type a number: "))
# print(know_number(number))

# Create a function that takes a list and return the amount of numbers that ends with the number 4


def end_with_4(lista: list[int]) -> int:
    counter = 0
    for i in lista:
        if abs(i) % 10 == 4:
            counter += 1
    return counter


lista = [1, 2, 43, 5, 76, 8, 9, 76, 4, 54, 66, 53]
print(end_with_4(lista))
