"""
1. Crear clase estudiante
2. Asignar atributos (Nombre, Edad, Grado)
3. Asignar métodos (estudiar) que imprima ('El estudiante (nombre) esta estudiando')
4. Crear un objeto estudiante y usar el método estudiar()
5. Se debe interactuar con el usuario y este debe brindar los atributos
6. Al escribir 'estudiar', usar el método estudiar() - [No case sensitive] 
"""


## Make a class
class Estudiante:
    ## Constructor method
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def print_study(self):
        print(f"El estudiante {self.name.capitalize()} está estudiando")

    def __format__(self, __format_spec: str) -> str:
        pass


name = input("Ingrese su nombre: ")
age = input("Ingrese su edad: ")
grade = input("Ingrese su grado: ")

estudiante = Estudiante(name, age, grade)


while True:
    status = input("Ingrese su estado: ")
    if status.capitalize() == "Estudiar":
        estudiante.print_study()
        break
