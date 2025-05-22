import os  
os.system('cls')
filas = 2
columnas = 2
matriz = []


for i in range (filas):
    matriz.append([])
    for j in range (columnas):
        valor = int(input(f"Inngrese el valor de la fila ({i+1}), ({j+1}) \n-> "))
        matriz[i].append(valor)
        os.system('cls')
print("La matriz es: ")
for fila in matriz:
        print(fila)

matriz_b = []
for i in range (filas):
    matriz_b.append([])
    for j in range (columnas):
        valor = int(input(f"Inngrese el valor de la fila ({i+1}), ({j+1}) \n-> "))
        matriz_b[i].append(valor)
        os.system('cls')
print("La matriz es: ")
for fila in matriz_b:
        print(fila)

matriz_c = []
for i in range (filas):
    matriz_c.append([])
    for j in range (columnas):
        valor = matriz[i][j] + matriz_b[i][j]
        matriz_c[i].append(valor)
        os.system('cls')
print("La matriz suma es: ")
for fila in matriz_c:
        print(fila)
