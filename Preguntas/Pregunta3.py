import math

class Circulo:
    def __init__(self, radio):
        self.radio = radio

    def calcular_area(self):
        area = math.pi * (self.radio ** 2)
        return area

def main():
    while True:
        try:
            radio_str = input("Ingrese el radio del círculo: ")
            radio = float(radio_str)
            if radio > 0:
                circulo = Circulo(radio)
                area = circulo.calcular_area()
                print("El área del círculo con radio", radio, "es:", area)
                break
            else:
                print("Error: el radio debe ser un número positivo.")
        except ValueError:
            print("Error: asegúrese de ingresar un número válido para el radio.")

if __name__ == "__main__":
    main()

