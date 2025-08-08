parrticipante={}
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
        cantidad=int(input("Ingrese la cantidad de corredores que habran: "))
        for i in range(cantidad):
            print(f"Ingrese datos de corredor #{i+1} ")
            dorsal=input("Ingrese su dorsal: ")
            nombre=input("Ingrese su nombre completo: ")
            edad=int(input("Ingrese su edad: "))
            categoria=input("Ingrese la categoria donde competira: ")
            parrticipante[nombre]={
                "dorsal":dorsal,
                "edad":edad,
                "categoria":categoria
            }

    def Ordene