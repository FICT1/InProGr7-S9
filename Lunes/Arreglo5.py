#Leer x cantidad numeros y decir cuantos son pares y cuantos son impares
suma_pares = 0
suma_impares = 0
numeros = []
import os
os.system('cls')
while True:
    numero = int(input(f"Ingrese un número \n-> "))
    numeros.append(numero)

    resp = input(f"¿Desea ingresar otro número? (S/N) \n-> ")
    if resp.upper() == 'N':
        False
        break
for numero in numeros:
    if numero % 2 == 0:
        suma_pares += 1
    elif numero % 2 != 0:
        suma_impares += 1
print(f"La cantidad de numeros pares es: {suma_pares}")
print(f"La cantidad de numeros impares es: {suma_impares}")