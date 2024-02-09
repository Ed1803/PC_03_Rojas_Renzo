# PREGUNTA 2
def main():
    while True:
        calificaciones_str = input("Ingrese las calificaciones separadas por comas: ")
        # Dividir la cadena en calificaciones individuales
        calificaciones = calificaciones_str.split(',')
        calificaciones_enteros = []

        try:
            for calificacion in calificaciones:
                calificacion_entero = int(calificacion)
                calificaciones_enteros.append(calificacion_entero)
            break

        except ValueError:
            # Capturar error si la conversión a entero falla
            print("Error: Asegúrese de ingresar solo números separados por comas.")
            continue

    print("Lista de calificaciones:", calificaciones_enteros)

if __name__ == "__main__":
    main()