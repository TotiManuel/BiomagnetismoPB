from Funciones import CargaDatos, Venta, Reembolso

def cargaDatos():
    totalProductos = CargaDatos.main()
    return totalProductos

def main():
    datosCargados = cargaDatos()
    venta = Venta.main(datosCargados, "Gorra", 12.50, "U")
    reembolso = Reembolso.main(datosCargados, "Gorra", 12.50, "U")
if __name__ == "__main__":
    main()
