class Cuadrado:
    def __init__(self, lado):
        self.lado = lado

    def calcular_area(self):
        area = (self.lado ** 2)
        return area

def main():
    while True:
        try:
            radio_str = input("Ingrese el lado del cuadrado: ")
            radio = float(radio_str)
            if radio > 0:
                cuadrado = Cuadrado(radio)
                area = cuadrado.calcular_area()
                print("El área del cuadrado es:", area)
                break
            else:
                print("Error: el lado debe ser un numero positivo.")
        except ValueError:
            print("Error: asegúrese de ingresar un número válido para el lado .")

if __name__ == "__main__":
    main()