def quicksort_nombre(lista):
    if len(lista) <= 1:
        return lista
    else:
        pivote = lista[0]
        menores = [x for x in lista[1:] if x["nombre"].lower() < pivote["nombre"].lower()]
        iguales = [x for x in lista if x["nombre"].lower() == pivote["nombre"].lower()]
        mayores = [x for x in lista[1:] if x["nombre"].lower() > pivote["nombre"].lower()]
        return quicksort_nombre(menores) + iguales + quicksort_nombre(mayores)

def quicksort_edad(lista):
    if len(lista) <= 1:
        return lista
    else:
        pivote = lista[0]
        menores = [x for x in lista[1:] if x["edad"] < pivote["edad"]]
        iguales = [x for x in lista if x["edad"] == pivote["edad"]]
        mayores = [x for x in lista[1:] if x["edad"] > pivote["edad"]]
        return quicksort_edad(menores) + iguales + quicksort_edad(mayores)

participantes=[]
def agregar_participantes():
    cantidad = int(input("¿Cuántos participantes desea agregar? "))
    for i in range(cantidad):
        print(f"\nParticipante #{i + 1}")
        while True:
            dorsal = input("Número de dorsal: ")
            if any(p["dorsal"] == dorsal for p in participantes):
                print("Ese dorsal ya está registrado. Ingrese uno diferente.")
            else:
                break
        nombre = input("Nombre completo: ")
        edad = int(input("Edad: "))
        categoria = input("Categoría (juvenil, adulto, máster): ")
        participante={
            "dorsal": dorsal,
            "nombre":nombre,
            "edad": edad,
            "categoria":categoria
        }
        participantes.append(participante)
        print("Participantes agregados correctamente")

def mostrar_participantes(lista):
    for p in lista:
        print(f"- {p['nombre']} (Dorsal {p['dorsal']}, Edad {p['edad']}, Categoría: {p['categoria']})")

while True:
    print("---Menu---")
    print("1. Agregar participantes")
    print("2. Mostrar orden de participantes por nombre")
    print("3. Mostrar oreden de participnates por edad")
    print("4. Salir")
    opcion=input("Seleccione una opcion: ")
    match opcion:
        case "1":
            agregar_participantes()
        case "2":
            quicksort_nombre()
            mostrar_participantes()
        case "3":
             quicksort_edad()
             mostrar_participantes()
        case "4":
            print("Saliendo de registro de corredores")
            break
        case "_":
            print("Opcion no valida vuelva a intentar")