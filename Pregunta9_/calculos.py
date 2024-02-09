# calculos.py
import operaciones

def obtener_numero(mensaje):
    while True:
        try:
            num = float(input(mensaje))
            return num
        except ValueError:
            print("Error: Por favor, ingrese un número válido.")

def ejecutar_operacion(operacion):
    while True:
        num1 = obtener_numero("Ingrese el primer número: ")
        num2 = obtener_numero("Ingrese el segundo número: ")
        try:
            resultado = operacion(num1, num2)
            break
        except ZeroDivisionError:
            print("Error: No es posible dividir entre cero.")

print("Se realizara la Operacion de Suma")
ejecutar_operacion(operaciones.suma)

print("Se realizara la Operacion de Resta")
ejecutar_operacion(operaciones.resta)

print("Se realizara la Operacion de Producto")
ejecutar_operacion(operaciones.producto)

print("Se realizara la Operacion de División")
ejecutar_operacion(operaciones.division)
