## Make a class
class Celular:
    def __init__(self, brand, model, camera):
        self.brand = brand
        self.model = model
        self.camera = camera

    def call(self):
        print(f"Estas haciendo una llamada a un {self.model}")

    def cut_call(self):
        print(f"Cortaste la llamada a un {self.model}")


celular1 = Celular("Samsung", "S230", "42MP")
print(celular1.brand)
print(celular1.cut_call())


## Exercises ##

