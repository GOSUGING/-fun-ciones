def validar_listas_numeros(listas_numeros):
    numeros_validados = []
    for numero_str in listas_numeros:
        try:
            numero = int(numero_str)
            numeros_validados.append(numero)
        except ValueError:
            print("El valor", numero_str,"no es un numero entero")
            return None
    return numeros_validados

def identificar_pares_impares(listas_numeros):
    numeros_pares = []
    numeros_impares = []
    for numero in listas_numeros:
        if numero % 2 == 0:
            numeros_pares.append(numero)
        else:
            numeros_impares.append(numero)
    return numeros_pares, numeros_impares

def mostrar_resultados(numeros_pares, numeros_impares):
    print("Numeros pares:")
    for numero in numeros_pares:
        print(numero)
    print("\nNumeros impares")
    for numero in numeros_impares:
        print(numero)

lista_numeros_str = input("Ingresar lista de numeros separados por un espacio: ")
lista_numeros = lista_numeros_str.split()

while True:
    numero_validados = validar_listas_numeros(lista_numeros)
    if numero_validados:
        break
    else:
        lista_numeros_str = input("Lista no valida, intente nuevamente: ")
        lista_numeros = lista_numeros_str.split()

numeros_pares, numeros_impares = identificar_pares_impares(numero_validados)

mostrar_resultados(numeros_pares, numeros_impares)