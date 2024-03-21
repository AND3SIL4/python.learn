"""
  MRO: method resolution order 
  (orden en Python donde se busca un método en la jerarquía de clases)
"""


## Clase padre
class A:
    def hablar(self):
        return "Hola desde A"


class B(A):
    def hablar(self):
        return "Hola desde B"


class C(A):
    def hablar(self):
        return "Hola desde C"


class D(B, C):
    pass


##* Se prioriza la primera clase que se hereda
d = D()
## print(d.hablar())

## Saber la jerarquía de python ejecutando métodos de las clases
print(D.mro())