def contar_letras(cadena):
    contador = {}
    for letra in cadena:
        if letra in contador:
            contador[letra] += 1
        else:
            contador[letra] = 1
    return contador

cadena = input("Ingrese una cadena: ")
resultado = contar_letras(cadena)
print(resultado)
