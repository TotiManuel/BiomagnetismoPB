from Funciones import CargaDatos, Venta, Reembolso, AgregarProducto
import tkinter as tk
def cargaDatos():
    totalProductos = CargaDatos.main()
    return totalProductos
def venta(datosCargados):
    venta = Venta.main(datosCargados)
def reembolso(datosCargados):
    reembolso = Reembolso.main(datosCargados)
def agregarProducto(datosCargados):
    productoagregado = AgregarProducto.main(datosCargados)
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

    botonVenta = tk.Button(text="Agregar Venta", command=lambda: venta(datosCargados))
    botonVenta.pack()

    botonReembolso = tk.Button(text="Agregar Reembolso", command=lambda: reembolso(datosCargados))
    botonReembolso.pack()

    botonAgregarProducto = tk.Button(text="Agregar Producto", command=lambda: agregarProducto(datosCargados))
    botonAgregarProducto.pack()

    root.mainloop()
    
if __name__ == "__main__":
    main()
