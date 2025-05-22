# 2. Se desea realizar un programa en donde se capture 
# el nombre y 
# tres calificaciones para
# 5 estudiantes de la facultad de Ingeniería, 
# y después se pueda procesar dándonos el
# promedio final de cada uno de los alumnos, 
# el resultado se mostrará en pantalla.



#Franklin Callejas
import os
import time 
os.system('cls || clear')

def promedio(calif1, calif2, calif3):
    return (calif1 + calif2 + calif3) / 3

def menu():
    print("")
    print("-----Menú de opciones-----")
    print("1. Capturar datos")
    print("2. Mostrar promedios")
    print("3. Salir")
    print("")
    try:
        opcion = int(input("Ingrese una opción\n-> "))
        return opcion
    except ValueError:
        return -1
    
def submenu():
    while True:
        print("\n¿Qué desea hacer ahora?")
        print("1. Volver al menú")
        print("2. Salir del programa")
        try:
            opcion = int(input("Ingrese una opción\n-> "))
            if opcion == 1:
                return True  
            elif opcion == 2:
                return False  
            else:
                print("Opción no válida. Por favor, seleccione 1 o 2.")
                time.sleep(2)
                os.system('cls || clear')
        except ValueError:
            print("Entrada no válida. Por favor, ingrese un número (1 o 2).")
            time.sleep(2)
            os.system('cls || clear')

def main():
    while True:
        os.system('cls || clear')
        opcion = menu()
        if opcion == 1:
            for i in range(5):
                print(f"*** Estudiante {i+1} ***")
                nombre = input("Ingrese el nombre del estudiante: ")
                print("")
                calif1 = float(input("Ingrese la primera calificación: "))
                calif2 = float(input("Ingrese la segunda calificación: "))
                calif3 = float(input("Ingrese la tercera calificación: "))
                print("")
                # Guardar el nombre y las calificaciones en las listas
                nombres[i] = nombre
                calificaciones[i] = [calif1, calif2, calif3]
                promedios[i] = promedio(calif1, calif2, calif3)
            time.sleep(3)
            if not submenu():
                break
        elif opcion == 2:
            # Verificar si se han ingresado estudiantes (todos promedios son 0)
            if all(promedio == 0 for promedio in promedios):
                print("No ha ingresado ningún estudiante")
            else:
                for i in range(5):
                    if promedios[i] != 0:  # Solo mostrar estudiantes con datos
                        print(f"Estudiante: {nombres[i]}")
                        print(f"Calificaciones: {calificaciones[i][0]}, {calificaciones[i][1]}, {calificaciones[i][2]}")
                        print(f"Promedio: {promedios[i]:.2f}")
                        print("")
            time.sleep(3)
            if not submenu():
                break
        elif opcion == 3:
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción del menú.")
            time.sleep(2)
            os.system('cls || clear')

# Inicializar las listas para nombres, calificaciones y promedios
nombres = [""] * 5
calificaciones = [[0, 0, 0] for _ in range(5)]
promedios = [0] * 5

# Llamar a la función principal
main()