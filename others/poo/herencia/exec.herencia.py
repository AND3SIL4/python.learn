"""
  Ejercicio de herencia y de super()
  - Crear un sistema de una escuela. En este sistema, vamos a tener dos clases principales:
  Persona y Estudiante. 
  - La clase Persona tendrá los atributos de nombre y edad y un método 
  que imprima el nombre y la edad de la persona. 
  - La clase Estudiante heredará de la clase Persona 
  - Y también un atributo adicional: grado y un método que imprima el grado del estudiante.

  Deberás utilizar super en el método de inicialización (init) para reutilizar el código de la clase padre 
  (Persona). Luego crea una instancia de la clase Estudiante e imprime sus atributos y utiliza sus métodos
  para asegurarte de que todo funciona correctamente.
"""


class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def imprimir_datos(self):
        return f"Mi nombre es {self.nombre} y tengo {self.edad} años"


class Estudiante(Persona):
    def __init__(self, nombre, edad, grado):
        super().__init__(nombre, edad)
        self.grado = grado

    def imprimir_grado(self):
        return f"Mi grado es: {self.grado}"


felipe = Estudiante("Felipe", 21, 30)

print(felipe.imprimir_datos())
print(felipe.imprimir_grado())


"""
  Segundo ejercicio (herencia multiple y MRO):

  Imagina que estas modelando animales en un zoológico. 
  
  - Crear tres clases: Animal, Mamífero, y Ave
  - La clase Animal debe tener un método llamado comer
  - La clase Mamífero debe tener un método llamado amamantar 
  - La clase Ave un método llamado volar

  Ahora crea una clase Murciélago que herede de Mamífero y Ave en ese orden
  - Por lo tanto debe ser capaz de amamantar y volar ademas de comer

  - Finalmente juega con el orden de herencia de la clase Murciélago y observa como cambia el MRO
  - Usa super()  
"""


class Animal:
    def comer(self):
        return "Soy un animal y estoy comiendo"


class Mamifero(Animal):
    def amamantar(self):
        return "Soy un mamífero y estoy amantando"


class Ave(Animal):
    def volar(self):
        return "Soy un ave y estoy volando"


class Murcielago(Mamifero, Ave):
    pass


murcielago = Murcielago()
print(murcielago.comer())
print(murcielago.amamantar())
print(murcielago.volar())
