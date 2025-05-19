edades = [18, 17, 17, 16, 20, 27, 19, 21]
print(edades)
# Ordenar el arreglo
edades.sort()
print(edades)
# Buscar un elemento en el arreglo
edades.sort(reverse=True)
print(edades)

import statistics as st
#Mostrar la media
media = st.mean(edades)
print(f"La media de las edades es: {media}") #Promedio

#Mostrar la moda
moda = st.mode(edades)
print(f"La moda de las edades es: {moda}") #Valor que más se repite
