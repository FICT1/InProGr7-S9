estudiantes = ["Jorge Picado", "Franklin Callejas", "Josue Espinozala", "Joshua Saenz"]
tamanio = len(estudiantes)
print(f"El tamaño del arreglo es: {tamanio}")
#recorrer los elementos del arreglo
for estudiante in estudiantes:
    print(f"{estudiante} tiene {len(estudiante)} caracteres")
    vocales = "aeiou"
    sumavocales = 0
    for letra in estudiante:
        if letra.lower() in vocales:
            sumavocales += 1
    for letra in estudiante:
        print(f"{letra.upper()*2}")
    print(f"{estudiante} tiene {sumavocales} vocales")