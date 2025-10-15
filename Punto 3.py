def eliminar_vocales_repetidas(cadena):
    resultado = ""
    vocales_utilizadas = ""

    for caracter in cadena:
        codigo = ord(caracter)

        if 65 <= codigo <= 90:
            codigo += 32

        if codigo == 97 or codigo == 101 or codigo == 105 or codigo == 111 or codigo == 117:
            vocal = chr(codigo)
            distinta = True

            for v in vocales_utilizadas:
                if v == vocal:
                    distinta = False

            if distinta:
                vocales_utilizadas += vocal
                resultado += caracter
        else:
            resultado += caracter

    return resultado

texto = input("Ingrese un texto: ")
print(eliminar_vocales_repetidas(texto))