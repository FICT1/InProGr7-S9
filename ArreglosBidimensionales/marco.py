#contar elementos mayores que un numero
#dado una lista de 10 numeros, contar cuántos son mayores que 50



import os
os.system('cls || clear')

def contar_mayores(lista, numero):
    contador = 0
    for elemento in lista:
        if elemento > numero:
            contador += 1
    return contador


numeros = int(input("Ingrese 10 numeros: "))
lista_numeros = []
for i in range(10):
    numero = int(input(f"Ingrese el numero {i+1}: "))
    lista_numeros.append(numero)


