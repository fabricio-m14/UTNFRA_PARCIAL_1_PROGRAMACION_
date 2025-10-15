array_aleatorio = [None] * 10

respuesta = "si"

print(f"Array antes: {array_aleatorio}")

while respuesta == "si":
    while True:
        ingresa_numero = input("Ingrese un número: ")
        if ingresa_numero == "":
            print("Debe ingresar un caracter válido.")
            continue
        cadena_sin_punto = ingresa_numero.replace(".", "", 1)
        if cadena_sin_punto.isdigit() and ingresa_numero.count(".") <= 1:
            numero = float(ingresa_numero)
            break
        else:
            print("Reingrese un valor numérico")

    while True:
        indice_input = input(f"Ingrese la posición del número ingresado (0-{len(array_aleatorio)-1}): ")
        if indice_input == "":
            print("Debe ingresar un valor.")
            continue
        if not indice_input.isdigit():
            print("Debe ingresar un número entero.")
            continue
        indice = int(indice_input)
        if 0 <= indice < len(array_aleatorio):
            break
        else:
            print(f"El índice debe estar entre 0 y {len(array_aleatorio)-1}.")

    array_aleatorio[indice] = numero
    respuesta = input("¿Desea continuar?: Si/No ")

for i in range(len(array_aleatorio)):
    if array_aleatorio[i] != None:
        print(f"Numero = {array_aleatorio[i]} - Índice: {i}")
print(f"Arreglo cargado aleatoriamente: {array_aleatorio}")