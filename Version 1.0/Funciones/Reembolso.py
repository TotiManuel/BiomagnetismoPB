from Class.ClassProducto import Producto
import tkinter as tk
def reembolsarProducto(datosCargados):
    pass
    #for i in datosCargados:
    #    if i[0] == nombrepedido:
    #        if float(i[1]) == float(preciopedido):
    #            if i[2] == tallapedido:
    #                productocreado = Producto(i[0], i[1], i[2], i[3])
    #                productocreado.setReembolso(1)
    #                print("Producto Reembolsado")
    #return(productocreado)
def main(datosCargados):
    root = tk.Tk()
    root.title("Registro de Ventas")
    root.geometry("400x500+0+0")

    barraMenu = tk.Menu(root)
    menuArchivo = tk.Menu(barraMenu, tearoff=0)

    menuArchivo.add_command(label="Sin Programar", command=lambda: reembolsarProducto(datosCargados))
    barraMenu.add_cascade(label="Sin Programar", menu=menuArchivo)

    root.config(menu=barraMenu)

    labelProducto = tk.Label(root, text="Producto: ")
    labelProducto.pack()

    labelTalla = tk.Label(root, text="Talla: ")
    labelTalla.pack()

    labelPrecio = tk.Label(root, text="Precio: ")
    labelPrecio.pack()

    root.mainloop()
if __name__=="__main__":
    main()
