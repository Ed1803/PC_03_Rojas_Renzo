class Producto:
    def __init__(self, nombre, categoria, precio, año):
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio
        self.año = año

    def __str__(self):
        return f"{self.nombre} \n-Categoria: ${self.categoria} \n-Precio: ${self.precio} \n- Año: {self.año}"


class Catalogo:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def mostrar_productos(self):
        print("Lista de productos:")
        for producto in self.productos:
            print(producto)

    def filtrar_por_año(self, año):
        print(f"Productos del año {año}:")
        for producto in self.productos:
            if producto.año == año:
                print(producto)

# Ejemplo de uso:
def main():
    catalogo = Catalogo()
    producto1 = Producto("Mochila Paxton", "Utiles Escolares",200, 2022)
    catalogo.agregar_producto(producto1)
    producto2 = Producto("Limpiavidrios Sapolio","Limpieza", 10, 2014)
    catalogo.agregar_producto(producto2)
    producto3 = Producto("Galletas Picaras","Alimentos", 30, 2016)
    catalogo.agregar_producto(producto3)

    catalogo.mostrar_productos()

    año = int(input("Ingrese el año para filtrar los productos: "))
    catalogo.filtrar_por_año(año)

if __name__ == "__main__":
    main()