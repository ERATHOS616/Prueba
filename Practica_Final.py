class Producto:
    def __init__(self, nombre, categoria, precio, cantidad):
        self.__nombre = nombre
        self.__categoria = categoria
        self.__precio = precio
        self.__cantidad = cantidad

    # Getters
    def get_nombre(self):
        return self.__nombre

    def get_categoria(self):
        return self.__categoria

    def get_precio(self):
        return self.__precio

    def get_cantidad(self):
        return self.__cantidad

    # Setters
    def set_precio(self, precio):
        if precio > 0:
            self.__precio = precio
        else:
            raise ValueError("El precio debe ser mayor que 0")

    def set_cantidad(self, cantidad):
        if cantidad >= 0:
            self.__cantidad = cantidad
        else:
            raise ValueError("La cantidad debe ser mayor o igual que 0")

    # Representación en texto del producto
    def __str__(self):
        return f"Categoría: {self.__categoria}, Precio: {self.__precio}, Cantidad: {self.__cantidad}"


class Inventario:
    def __init__(self):
        self.__productos = []

    # Agregar un nuevo producto al inventario
    def agregar_producto(self, producto):
        for p in self.__productos:
            if p.get_nombre() == producto.get_nombre():
                raise ValueError("El producto ya existe en el inventario")
        self.__productos.append(producto)

    # Actualizar el precio o cantidad de un producto existente
    def actualizar_producto(self, nombre, nuevo_precio=None, nueva_cantidad=None):
        for p in self.__productos:
            if p.get_nombre() == nombre:
                if nuevo_precio is not None:
                    p.set_precio(nuevo_precio)
                if nueva_cantidad is not None:
                    p.set_cantidad(nueva_cantidad)
                return
        raise ValueError("Producto no encontrado")

    # Eliminar un producto del inventario
    def eliminar_producto(self, nombre):
        for p in self.__productos:
            if p.get_nombre() == nombre:
                self.__productos.remove(p)
                return
        raise ValueError("Producto no encontrado")

    # Mostrar todos los productos del inventario
    def mostrar_inventario(self):
        if not self.__productos:
            print("El inventario está vacío.")
        for p in self.__productos:
            print(f"Producto: {p.get_nombre()} - {p}")

    # Buscar un producto por nombre
    def buscar_producto(self, nombre):
        for p in self.__productos:
            if p.get_nombre() == nombre:
                return p
        raise ValueError("Producto no encontrado")


# Función principal para ejecutar la aplicación desde la terminal
def main():
    inventario = Inventario()

    while True:
        print("\n--- Menú de Inventario ---")
        print("1. Agregar producto")
        print("2. Actualizar producto")
        print("3. Eliminar producto")
        print("4. Mostrar inventario")
        print("5. Buscar producto")
        print("6. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            nombre = input("Ingrese el nombre del producto: ")
            categoria = input("Ingrese la categoría del producto: ")
            precio = float(input("Ingrese el precio del producto: "))
            cantidad = int(input("Ingrese la cantidad en stock: "))

            try:
                producto = Producto(nombre, categoria, precio, cantidad)
                inventario.agregar_producto(producto)
                print(f"Producto '{nombre}' agregado exitosamente.")
            except ValueError as e:
                print(f"Error: {e}")

        elif opcion == '2':
            nombre = input("Ingrese el nombre del producto a actualizar: ")
            nuevo_precio = input("Ingrese el nuevo precio (dejar en blanco para no cambiar): ")
            nueva_cantidad = input("Ingrese la nueva cantidad (dejar en blanco para no cambiar): ")

            nuevo_precio = float(nuevo_precio) if nuevo_precio else None
            nueva_cantidad = int(nueva_cantidad) if nueva_cantidad else None

            try:
                inventario.actualizar_producto(nombre, nuevo_precio, nueva_cantidad)
                print(f"Producto '{nombre}' actualizado exitosamente.")
            except ValueError as e:
                print(f"Error: {e}")

        elif opcion == '3':
            nombre = input("Ingrese el nombre del producto a eliminar: ")
            try:
                inventario.eliminar_producto(nombre)
                print(f"Producto '{nombre}' eliminado exitosamente.")
            except ValueError as e:
                print(f"Error: {e}")

        elif opcion == '4':
            inventario.mostrar_inventario()

        elif opcion == '5':
            nombre = input("Ingrese el nombre del producto a buscar: ")
            try:
                producto = inventario.buscar_producto(nombre)
                print(f"Producto encontrado: {producto}")
            except ValueError as e:
                print(f"Error: {e}")

        elif opcion == '6':
            print("Saliendo del sistema...")
            break

        else:
            print("Opción no válida. Por favor, intente de nuevo.")


if __name__ == "__main__":
    main()
