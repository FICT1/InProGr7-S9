
import os 
os.system('cls')
filas = int(input("Cuantas filas desea ingresar? \n-> "))
columnas = int(input("Cuantas columnas desea ingresar? \n-> "))
matriz = []

for i in range (filas):
    matriz.append([])
    for j in range (columnas):
        valor = int(input(f"Ingrese el valor de la fila ({i+1}), ({j+1}) \n-> "))
        matriz[i].append(valor)

print("La matriz es: ")
for fila in matriz:
        print(fila)

escala = int(input("Desea hacerle escala a la matriz? \n-> "))
matriz_escala = []
for i in range (filas):
    matriz_escala.append([])
    for j in range (columnas):
        valor = matriz[i][j] * escala
        matriz_escala[i].append(valor)

print("La matriz escala es: ")
for fila in matriz_escala:
        print(fila)


