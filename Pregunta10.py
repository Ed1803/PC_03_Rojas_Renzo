from Preguntas import Pregunta4
from Preguntas import Pregunta3
from ArchivoExtra import Cuadradito

def menu():
    while True:
        print("\nMenú:")
        print("1. Calcular el área de un círculo")
        print("2. Calcular el área de un rectángulo")
        print("3. Calcular el área de un cuadrado")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            Pregunta3.main() 
            break  
        elif opcion == '2':
           Pregunta4.calcular_area_rectangulo() 
           break
        elif opcion == '3':
            Cuadradito.main()
            break
        elif opcion == '4':
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción del menú.")

if __name__ == "__main__":
    menu()
