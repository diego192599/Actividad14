
class Participantes:
    def __init__(self,dorsal,nombre,edad,categoria):
        if not dorsal or not nombre or edad < 0 or not categoria:
            raise ValueError("Datos no válidos")
        self.dorsal=dorsal
        self.nombre=nombre
        self.edad=edad
        self.categoria=categoria
    def __str__(self):
        return (f"{self.dorsal}- Nombre: {self.nombre}- Edad: {self.edad} y Categoria: {self.categoria}")

participante=[]

def agregar():
    cantidad = int(input("Ingrese la cantidad de corredores que habran: "))
    for i in range(cantidad):
        print(f"Ingrese datos de corredor #{i + 1} ")
        dorsal = input("Ingrese su dorsal: ")
        nombre = input("Ingrese su nombre completo: ")
        edad = int(input("Ingrese su edad: "))
        categoria = input("Ingrese la categoria donde competira: ")
        participantes=Participantes(dorsal,nombre,edad,categoria)
        participante.append(participantes)

def orden(lista):
    if len(lista)<=1:
        return lista
    else:
        pivote=[0][1]
        menor=[x for x in lista[1:] if x[1]<pivote]
        igual=[x for x in lista if x[1]==pivote]
        mayor=[x for x in lista[1:] if x[1]>pivote]

