lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(lista)

# lista.reverse()
print(lista)

for i in range(0, 10, -1):
    print(i)

result = lista[len(lista) - 1:: -1]
print(result)

another = lista[::-1]
print(another)

variable = " ".join([str(value) for value in lista])
print(variable)


def function_do_nothing() -> None: ...


print("After function that do nothing")
