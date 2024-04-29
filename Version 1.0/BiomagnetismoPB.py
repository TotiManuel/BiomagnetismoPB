from Funciones import AgregarProducto
from Class.ClassProducto import Producto
import tkinter as tk
from tkinter import ttk, messagebox

def cargaDatos():
    with open ("Productos.txt") as Productos:
        totalProductos = []
        productoTupla = Productos.readlines()
        for i in productoTupla:
            producto = i.strip().split(",")
            if producto[0].lower() != "producto":
                agregarProducto = Producto(producto[0], producto[1], producto[2], producto[3])
                totalProductos.append(agregarProducto)
    return totalProductos

def actualizar(*args):
    for i in datosCargados:
        if comboboxProducto.get() == i.getProducto():
            talla = i.getTalla()
            precio = float(i.getPrecio()) * float(SpinboxCantidad.get())
    entryTalla.config(state="normal")
    entryPrecio.config(state="normal")
    entryTalla.delete(0, tk.END)
    entryTalla.insert(tk.END, talla)
    entryPrecio.delete(0, tk.END)
    entryPrecio.insert(tk.END, "$" + str(precio))
    entryTalla.config(state="readonly")
    entryPrecio.config(state="readonly")

def buscarNombres():
    nombres = []
    for i in datosCargados:
        nombres.append(i.getProducto())
    return(nombres)

def venta(nombrepedido, tallapedido, cantidadpedido, preciopedido):
    for i in datosCargados:
        if i.getProducto() == nombrepedido:
            if i.getTalla() == tallapedido:
                i.setVendido(int(cantidadpedido))
                messagebox.showinfo("Producto Vendido", "El producto fue vendido con exito\nProducto: " + i.getProducto() + "\nTalla: " + i.getTalla() + "\nPrecio: " + preciopedido + "\nStock: " + str(i.getStock()) + "\nVentas: " + str(i.getVendido()))
    stockactual = i.getStock() - int(cantidadpedido)
    precioactual = float(preciopedido[1::])*float(cantidadpedido)
    with open("Ventas.txt", "+a") as venta:
        venta.write("\n--------------------\nProducto: " + nombrepedido + "\nTalla: " + tallapedido + "\nPrecio: " + str(precioactual) + "\nStock: " + str(stockactual) + "\nVentas: " + str(i.getVendido()) + "\n--------------------")

def reembolso():
    pass
    #for i in datosCargados:
    #    if i[0] == nombrepedido:
    #        if float(i[1]) == float(preciopedido):
    #            if i[2] == tallapedido:
    #                productocreado = Producto(i[0], i[1], i[2], i[3])
    #                productocreado.setReembolso(1)
    #                print("Producto Reembolsado")
    #return(productocreado)

def agregarProducto():
    productoagregado = AgregarProducto.main(datosCargados)

def main():
    #region principal
    global datosCargados, entryTalla, comboboxProducto, entryPrecio, SpinboxCantidad
    datosCargados = cargaDatos()
    root = tk.Tk()
    root.title("BioMagnetismo")

    barraMenu = tk.Menu(root)
    menuArchivo = tk.Menu(barraMenu, tearoff=0)
    menuTurnero = tk.Menu(barraMenu, tearoff=0)

    menuArchivo.add_command(label="Probar Venta", command=lambda: venta())
    menuArchivo.add_command(label="Probar Reembolso", command=lambda: reembolso())
    menuArchivo.add_command(label="Probar Agregar Producto", command=lambda: agregarProducto())
    barraMenu.add_cascade(label="Archivo", menu = menuArchivo)

    menuTurnero.add_command(label="Buscar Paciente", command=lambda: venta())
    menuTurnero.add_command(label="Turnero", command=lambda: reembolso())
    menuTurnero.add_command(label="Sin Programar", command=lambda: agregarProducto())
    barraMenu.add_cascade(label="Turnero", menu = menuTurnero)
    
    root.config(menu=barraMenu)

    notebook = ttk.Notebook(root)

    tab1 = ttk.Frame(notebook)
    tab2 = ttk.Frame(notebook)
    tab3 = ttk.Frame(notebook)
    tab4 = ttk.Frame(notebook)
    tab5 = ttk.Frame(notebook)

    notebook.add(tab1, text="Bienvenido")
    notebook.add(tab2, text="Ventas")
    notebook.add(tab3, text="Reembolso")
    notebook.add(tab4, text="Agregar Producto")
    notebook.add(tab5, text="Agregar Stock")
    #endregion

    #region Ventas
    frameProducto = ttk.Frame(tab2)
    frameProducto.pack(anchor="w", pady=5)

    frameTalla = ttk.Frame(tab2)
    frameTalla.pack(anchor="w", pady=5)

    frameCantidad = ttk.Frame(tab2)
    frameCantidad.pack(anchor="w", pady=5)

    framePrecio = ttk.Frame(tab2)
    framePrecio.pack(anchor="w", pady=5)

    labelProducto = tk.Label(frameProducto, text="Producto: ")
    labelProducto.pack(side="left")

    labelTalla = tk.Label(frameTalla, text="Talla: ")
    labelTalla.pack(side="left")

    labelCantidad = tk.Label(frameCantidad, text="Cantidad: ")
    labelCantidad.pack(side="left")

    labelPrecio = tk.Label(framePrecio, text="Precio: ")
    labelPrecio.pack(side="left")

    entryTalla = tk.Entry(frameTalla)
    entryTalla.insert(tk.END, "Talle")
    entryTalla.config(state="readonly")
    entryTalla.pack(side="right")

    comboboxProducto = ttk.Combobox(frameProducto, values=buscarNombres(), state="readonly")
    comboboxProducto.set("Productos")
    comboboxProducto.bind("<<ComboboxSelected>>", actualizar)
    comboboxProducto.pack(side="right")

    SpinboxCantidad = tk.Spinbox(frameCantidad, from_=1, to=100, state="readonly")
    SpinboxCantidad.bind("<<FocusOut>>", actualizar)
    SpinboxCantidad.pack(side="right")

    entryPrecio = tk.Entry(framePrecio, state="readonly")
    entryPrecio.pack(side="right")

    botonVender = tk.Button(tab2, text="Vender", command= lambda: venta(comboboxProducto.get(), entryTalla.get(), SpinboxCantidad.get(), entryPrecio.get()))
    botonVender.pack()
    #endregion

    #region Reembolsos
    frameProducto = ttk.Frame(tab3)
    frameProducto.pack(anchor="w", pady=5)

    frameTalla = ttk.Frame(tab3)
    frameTalla.pack(anchor="w", pady=5)

    frameCantidad = ttk.Frame(tab3)
    frameCantidad.pack(anchor="w", pady=5)

    framePrecio = ttk.Frame(tab3)
    framePrecio.pack(anchor="w", pady=5)

    labelProducto = tk.Label(frameProducto, text="Producto: ")
    labelProducto.pack(side="left")

    labelTalla = tk.Label(frameTalla, text="Talla: ")
    labelTalla.pack(side="left")

    labelCantidad = tk.Label(frameCantidad, text="Cantidad: ")
    labelCantidad.pack(side="left")

    labelPrecio = tk.Label(framePrecio, text="Precio: ")
    labelPrecio.pack(side="left")

    entryTalla = tk.Entry(frameTalla)
    entryTalla.insert(tk.END, "Talle")
    entryTalla.config(state="readonly")
    entryTalla.pack(side="right")

    comboboxProducto = ttk.Combobox(frameProducto, values=buscarNombres(), state="readonly")
    comboboxProducto.set("Productos")
    comboboxProducto.bind("<<ComboboxSelected>>", actualizar)
    comboboxProducto.pack(side="right")

    SpinboxCantidad = tk.Spinbox(frameCantidad, from_=1, to=100, state="readonly")
    SpinboxCantidad.bind("<<FocusOut>>", actualizar)
    SpinboxCantidad.pack(side="right")

    entryPrecio = tk.Entry(framePrecio, state="readonly")
    entryPrecio.pack(side="right")

    botonVender = tk.Button(tab3, text="Reembolsar", command= lambda: reembolso(comboboxProducto.get(), entryTalla.get(), SpinboxCantidad.get(), entryPrecio.get()))
    botonVender.pack()
    #endregion

    notebook.pack(expand=True, fill='both')

    root.mainloop()
    
if __name__ == "__main__":
    main()
