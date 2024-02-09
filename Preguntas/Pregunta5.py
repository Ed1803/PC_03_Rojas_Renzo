class Alumno:
    def __init__(self, nombre, numero_registro):
        self.nombre = nombre
        self.numero_registro = numero_registro
        self.edad = None
        self.notas = []

    def display(self):
        print("Nombre:", self.nombre)
        print("Número de registro:", self.numero_registro)
        if self.edad is not None:
            print("Edad:", self.edad)
        else:
            print("Edad: No definida")
        if self.notas:
            print("Notas:", self.notas)
        else:
            print("Notas: No definidas")

    def set_edad(self, edad):
        self.edad = edad

    def set_notas(self, notas):
        self.notas = notas

def main():
    nombre = input("Ingrese el nombre del alumno: ")
    numero_registro = input("Ingrese el número de registro: ")
    alumno = Alumno(nombre, numero_registro)
    alumno.set_edad(int(input("Ingrese la edad: ")))
    notas_str = input("Ingrese las notas por espacios: ")
    notas = [float(nota) for nota in notas_str.split()]
    alumno.set_notas(notas)
    
    alumno.display()

if __name__ == "__main__":
    main()
