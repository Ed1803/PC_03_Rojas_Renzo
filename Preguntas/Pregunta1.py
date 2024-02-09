#PREGUNTA 1
def main():
    bandera = True
    while bandera:
        try:
            fraccion = input("Ingrese una fracción en formato X/Y: ")

            # Dividir la entrada en numerador y denominador
            numerador, denominador = map(int, fraccion.split('/'))

            if numerador > denominador:
                raise ValueError("Error: X debe ser menor o igual a Y")
            elif denominador == 0:
                raise ZeroDivisionError("Error: Y debe ser diferente de 0.")
            # Si se pasan todas las verificaciones, cambiar la bandera a False
            bandera = False

        except ValueError as ve:
            # Capturar error de números no enteros, X mayor a Y o decimal en la entrada
            print(ve)
            continue
        except ZeroDivisionError as zde:
            # Capturar error de denominador igual a cero
            print(zde)
            continue
    resultado = round((numerador / denominador) * 100)

    if resultado < 1:
        print("Cantidad de combustible en el tanque: E")
    elif resultado > 99:
        print("Cantidad de combustible en el tanque: F")
    else:
        print("Cantidad de combustible en el tanque:", resultado, "%")

if __name__ == "__main__":
    main()