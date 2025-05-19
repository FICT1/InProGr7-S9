notas = [8, 3, 5, 9, 10, 8, 3, 8]
print(f"Notas: {notas}")
notas.append(7) # Agregar un elemento al final de la lista
notas.append(6)
notas.insert(0, 4) # Insertar un elemento en una posición específica
print(f"Notas: {notas}")

print(notas[2: len(notas)]) 