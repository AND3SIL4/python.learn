# def decorador(function):
#     def wrapper(*args, **kwargs):
#         return function(*args, **kwargs)
#     return wrapper

# @decorador
# def hola(string):
#     return string

# print(hola("Andres Felipe Silva"))

# list = [0, 1, 2, 3, 4, 5, 6, 8, 9]
# print(list)

# for i, idx in enumerate(list):
#     if i == 2:
#         del list[idx]
#         print("Elemento eliminado")
# print(list)

# list = [1, 23, 4, 5, 6, 89, 0]
# print(list)
# result = list.pop(1)
# print(list)
# print("The element deleted was:", result)

x = [1, 2, 3]
y = x 
y[0] = 4
print(x)