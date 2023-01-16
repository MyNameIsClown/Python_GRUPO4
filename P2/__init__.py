palabras = ["uno", "dos", "vaca", "viaje", "madrid", "uno"]

print("MENU")
print("1. Contar: Me pide una cadena, y me dice cuántas veces aparece en la lista.")
print("2. Modificar: Me pide una cadena, y otra cadena a modificar, y modifica todas las apariciones de la primera por la segunda en la lista.")
print("3. Eliminar: Me pide una cadena, y la elimina de la lista.")
print("4. Imprimir palabras")
print("5. Añadir palabras")
print("6. Terminar")

option = int(input("Porfavor, introduzca un valor\n"))


def cambiarPalabras(palabraACambiar, palabraDeIntercambio):
    numeroDeApariciones = palabras.count(palabraACambiar)
    if numeroDeApariciones.__eq__(0):
        print("No existe la palabra seleccionada")
    else:
        for n in range(0, numeroDeApariciones):
            indice = palabras.index(palabraACambiar)
            palabras[indice] = palabraDeIntercambio


def eliminarPalabra(palabraEliminar):
    numeroDeApariciones = palabras.count(palabraEliminar)
    if numeroDeApariciones.__eq__(0):
        print("No existe la palabra seleccionada")
    else:
        for n in range(0, numeroDeApariciones):
            palabras.remove(palabraEliminar)


while option.__ne__(6):
    if option.__eq__(1):
        cadena = input("Dime la cadena a buscar\n")
        print("Tu cadena aparece " + str(palabras.count(cadena)) + " veces")
    elif option.__eq__(2):
        palabraACambiar = input("¿Que cadena quieres cambiar?")
        palabraDeIntercambio = input("¿Porque cadena quieres intercambiar?")
        cambiarPalabras(palabraACambiar, palabraDeIntercambio)
    elif option.__eq__(3):
        palabraEliminar = input("¿Que palabra quieres eliminar?")
        eliminarPalabra(palabraEliminar)
    elif option.__eq__(4):
        print(palabras)
    elif option.__eq__(5):
        palabraAñadir = input("¿Que palabra quieres añadir?")
        palabras.append(palabraAñadir)
    else:
        print("Valor no valido")

    print("MENU")
    print("1. Contar: Me pide una cadena, y me dice cuántas veces aparece en la lista.")
    print("2. Modificar: Me pide una cadena, y otra cadena a modificar, y modifica todas las apariciones de la primera por la segunda en la lista.")
    print("3. Eliminar: Me pide una cadena, y la elimina de la lista.")
    print("4. Imprimir palabras")
    print("5. Añadir palabras")
    print("6. Terminar")

    option = int(input("Porfavor, introduzca un valor\n"))
