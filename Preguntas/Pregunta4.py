class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        area = self.base * self.altura
        return area

def calcular_area_rectangulo():
    while True:
            try:
                base_str = input("Ingrese la base del rectángulo: ")
                altura_str = input("Ingrese la altura del rectángulo: ")
                base = float(base_str)
                altura = float(altura_str)
                if base > 0 and altura > 0:
                    area = base * altura
                    print("El área del rectángulo es:", area)
                    break
                else:
                    print("Error: Las medidas deben ser números positivos.")
            except ValueError:
                print("Error: asegúrese de ingresar un número válido")

if __name__ == "__main__":
    calcular_area_rectangulo()
