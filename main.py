class Participantes:
    def __init__(self,dorsal,nombre,edad,categoria):
        if not dorsal or nombre or edad or categoria<0:
            raise ValueError("Datos no validos")
        self.dorsal=dorsal
        self.nombre=nombre
        self.edad=edad
        self.categoria=categoria
    def __str__(self):
        return (f"{self.dorsal}- Nombre: {self.nombre}- Edad: {self.edad} y Categoria: {self.categoria}")

    def agregar(self):