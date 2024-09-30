# Definición de la clase Producto
class Producto:
    def __init__(self, nombre, categoria, precio, cantidad):
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio
        self.cantidad = cantidad
    def get_nombre(self):
        return self.nombre

    
    def get_categoria(self):
        return self.categoria

    def get_precio(self):
        return self.precio

    def get_cantidad(self):
        return self.cantidad
    
    def actualizar_cantidad(self, nueva_cantidad):
        self.cantidad = nueva_cantidad

# Definición de la clase Inventario
class Inventario:
    def __init__(self):
        self.__productos = {}

    def agregar_producto(self, producto):
        if producto.get_nombre() in self.__productos:
            raise ValueError("El producto ya existe en el inventario.")
        self.__productos[producto.get_nombre()] = producto

    def mostrar_inventario(self):
        return self.__productos

    def buscar_producto(self, nombre_producto):
        return self.__productos.get(nombre_producto, None)

    def actualizar_producto(self, nombre_producto, nueva_cantidad):
        producto = self.buscar_producto(nombre_producto)
        if producto:
            producto.actualizar_cantidad(nueva_cantidad)
        else:
            raise ValueError("El producto no existe en el inventario.")


