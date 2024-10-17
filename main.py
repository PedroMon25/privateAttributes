# Importa la clase Venta desde el archivo venta.py
from classVenta import Venta

def main():
    # Crear una instancia de Venta
    venta = Venta()

    # Establecer los atributos de la venta
    venta.set_id_venta(101)
    venta.set_fecha('2024-10-16')
    venta.set_cliente('Maria Lopez')

    # Agregar productos a la venta
    venta.agregar_producto('A', 3, 50.00)  # 3 unidades de Producto A
    venta.agregar_producto('B', 1, 30.00)  # 1 unidad de Producto B
    venta.agregar_producto('C', 2, 20.00)  # 2 unidades de Producto C

    # Mostrar los detalles de la venta
    venta.mostrar_detalle()


if __name__ == "__main__":
    main()
