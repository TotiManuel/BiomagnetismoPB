from Funciones import CargaDatos, Venta, Reembolso, AgregarProducto
import tkinter as tk
def cargaDatos():
    totalProductos = CargaDatos.main()
    return totalProductos
def venta(datosCargados):
    venta = Venta.main(datosCargados, "Gorra", 12.50, "U")
def reembolso(datosCargados):
    reembolso = Reembolso.main(datosCargados, "Gorra", 12.50, "U")
def agregarProducto(datosCargados):
    productoagregado = AgregarProducto.main(datosCargados, "Banda", 11.00, "M", 7)
def main():
    datosCargados = cargaDatos()
    root = tk.Tk()
    root.title("BioMagnetismo")
    root.geometry("400x500+0+0")

    barraMenu = tk.Menu(root)
    menuArchivo = tk.Menu(barraMenu, tearoff=0)

    menuArchivo.add_command(label="Probar Venta", command=lambda: venta(datosCargados))
    menuArchivo.add_command(label="Probar Reembolso", command=lambda: reembolso(datosCargados))
    menuArchivo.add_command(label="Probar Agregar Producto", command=lambda: agregarProducto(datosCargados))
    barraMenu.add_cascade(label="Archivo", menu = menuArchivo)
    
    root.config(menu=barraMenu)

    root.mainloop()
    
if __name__ == "__main__":
    main()
