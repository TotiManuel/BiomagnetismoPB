from Funciones import CargaDatos, Venta, Reembolso, AgregarProducto
from Class.ClassProducto import Producto
def cargaDatos():
    totalProductos = CargaDatos.main()
    return totalProductos

def main():
    datosCargados = cargaDatos()
    x = 0
    while x != 1:
        venta = Venta.main(datosCargados, "Gorra", 12.50, "U")
        reembolso = Reembolso.main(datosCargados, "Gorra", 12.50, "U")
        productoagregado = AgregarProducto.main(datosCargados, "Banda", 11.00, "M", 7)
        x = x + 1
if __name__ == "__main__":
    main()
