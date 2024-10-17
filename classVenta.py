class Venta:

    __id_venta = None
    __fecha = None
    __cliente = None
    __productos = None  # Diccionario de productos vendidos
    __total = None

    def __init__(self):
        self.__productos = {}  # Inicializar el diccionario vacío

    # Getters para acceder a los atributos privados
    def get_id_venta(self):
        return self.__id_venta

    def get_fecha(self):
        return self.__fecha

    def get_cliente(self):
        return self.__cliente

    def get_productos(self):
        return self.__productos

    def get_total(self):
        return self.__total

    # Setters para modificar los atributos privados
    def set_id_venta(self, id_venta):
        self.__id_venta = id_venta

    def set_fecha(self, fecha):
        self.__fecha = fecha

    def set_cliente(self, cliente):
        self.__cliente = cliente

    # Método para agregar productos al diccionario
    def agregar_producto(self, producto, cantidad, precio_unitario):
        productos_validos = ['A', 'B', 'C']  # Solo se permiten estos 3 productos
        if producto in productos_validos:
            self.__productos[producto] = {'cantidad': cantidad, 'precio_unitario': precio_unitario}
            self.calcular_total()  # Recalcular el total cada vez que se agrega un producto
        else:
            print(f"Producto {producto} no permitido. Solo se permiten A, B o C.")

    # Método para calcular el total basado en cantidad y precio unitario
    def calcular_total(self):
        self.__total = sum(c['cantidad'] * c['precio_unitario'] for c in self.__productos.values())

    # Método para mostrar los detalles de la venta
    def mostrar_detalle(self):
        print(f"ID Venta: {self.__id_venta}")
        print(f"Fecha: {self.__fecha}")
        print(f"Cliente: {self.__cliente}")
        print("Productos:")
        for producto, detalles in self.__productos.items():
            print(f"  Producto: {producto}, Cantidad: {detalles['cantidad']}, Precio Unitario: ${detalles['precio_unitario']:.2f}")
        print(f"Total: ${self.__total:.2f}")
