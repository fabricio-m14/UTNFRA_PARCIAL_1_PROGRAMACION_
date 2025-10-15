array_aleatorio = [None] * 10
respuesta = "si"

def a_num(c):
    digitos = "0123456789"
    i = 0
    while i < 10:
        if c == digitos[i]:
            return i
        i += 1
    return -1

while respuesta == "si":
    while True:
        print("Ingrese un número: ")
        t = input()
        
        if len(t) == 0:
            print("Debe ingresar un valor.")
            continue

        s = 1
        if t[0] == "-":
            s = -1
            t = t[1:]

        entero = 0
        decimal = 0
        div = 1
        es_decimal = 0
        v = True
        i = 0
        while i < len(t):
            c = t[i]
            if c == ".":
                if es_decimal == 1:
                    v = False
                    break
                es_decimal = 1
            else:
                n = a_num(c)
                if n == -1:
                    v = False
                    break
                
                if es_decimal == 0:
                    entero = entero * 10 + n
                else:
                    decimal = decimal * 10 + n
                    div *= 10
            i += 1

        if v and not (len(t) == 0 or t == "." or t == "-." or (es_decimal == 1 and div == 1)):
            numero = s * (entero + decimal / div)
            break
        else:
            print("Número inválido.")

    while True:
        print("Ingrese posición (0-", len(array_aleatorio) - 1, "): ")
        t = input()
        
        if len(t) == 0:
            print("Debe ingresar un valor.")
            continue

        v = True
        indice = 0
        i = 0
        while i < len(t):
            n = a_num(t[i])
            if n == -1:
                v = False
                break
            indice = indice * 10 + n
            i += 1

        if v and 0 <= indice < len(array_aleatorio):
            break
        else:
            print("Índice inválido.")

    array_aleatorio[indice] = numero

    print("¿Desea continuar? (Si/No): ")
    respuesta = input()
    
    if respuesta == "no":
        respuesta = "no"
    else:
        respuesta = "si"

for i in range(len(array_aleatorio)):
    if array_aleatorio[i] != None:
        print(f"Numero = {array_aleatorio[i]} - Índice: {i}")
print("Arreglo cargado:", array_aleatorio)
