# """Herencia simple"""


# ## Clase padre
# class Person:
#     def __init__(self, name, age, nationality):
#         self.name = name
#         self.age = age
#         self.nationality = nationality

#     def talk(self):
#         print(f"My name is {self.name}")


# ## Clase que hereda de la clase padre (Person)
# class Employee(Person):
#     """Los métodos se pueden reescribir en la clase que hereda"""

#     def __init__(self, name, age, nationality, job, salary):
#         super().__init__(name, age, nationality)
#         self.job = job
#         self.salary = salary


# """Herencia jerárquica: varias clases heredan de una clase padre"""


# ## Clase padre
# class Person:
#     def __init__(self, name, age, nationality):
#         self.name = name
#         self.age = age
#         self.nationality = nationality

#     def talk(self):
#         print(f"My name is {self.name}")


# ## Clase que hereda de la clase padre (Person)
# class Employee(Person):
#     """Los métodos se pueden reescribir en la clase que hereda"""

#     def __init__(self, name, age, nationality, job, salary):
#         super().__init__(name, age, nationality)
#         self.job = job
#         self.salary = salary

# ## Clase que hereda de la clase padre (Person)
# class Student(Person):
#     """Los métodos se pueden reescribir en la clase que hereda"""

#     def __init__(self, name, age, nationality, job, salary):
#         super().__init__(name, age, nationality)
#         self.job = job
#         self.salary = salary


"""Herencia multiple: una clase hereda de varias clases"""


## Clase padre
class Person:
    def __init__(self, name, age, nationality):
        self.name = name
        self.age = age
        self.nationality = nationality

    def talk(self):
        print(f"My name is {self.name}")


## Clase que hereda de la clase padre (Person)
class Artist:
    """Los métodos se pueden reescribir en la clase que hereda"""

    def __init__(self, ability):
        self.ability = ability

    def greet_whit_ability(self):
        return f"Hola, mi habilidad es {self.ability}"


## Clase que hereda de la clase padre (Person, Artist)
class Employee(Person, Artist):
    """Para heredar de multiples clases se pone el nombre de la clase padre y luego el constructor"""

    def __init__(self, name, age, nationality, salary, ability):
        Person.__init__(self, name, age, nationality)
        Artist.__init__(self, ability)
        self.salary = salary
        self.ability = ability

    ## Para heredar métodos se utiliza la palabra reservada super()
    def introduce_yourself(self):
        return super().greet_whit_ability()


felipe = Employee("Felipe", 21, "Colombian", 120000, "desarrollar")
# print(felipe.introduce_yourself())

## Saber si una clase hereda de otra usando (issubclass)
herencia = issubclass(Employee, Artist)  ## True
herencia2 = issubclass(Artist, Person)  ## False


## Saber si un objeto y/o variable es una instancia de una clase usando (isinstance)
instancia = isinstance(felipe, Person)  ## True
instancia2 = isinstance(felipe, Artist)  ## True
print(instancia2)
