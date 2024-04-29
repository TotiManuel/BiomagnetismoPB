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
                agregarProducto = Producto(producto[0], producto[1], producto[2], producto[3], producto[4], producto[5])
                totalProductos.append(agregarProducto)
    return totalProductos

def actualizar_venta(*args):
    for i in datosCargados:
        if comboboxProducto_venta.get() == i.getProducto():
            talla = i.getTalla()
            precio = float(i.getPrecio()) * float(SpinboxCantidad_venta.get())
    entryTalla_venta.config(state="normal")
    entryPrecio_venta.config(state="normal")
    entryTalla_venta.delete(0, tk.END)
    entryTalla_venta.insert(tk.END, talla)
    entryPrecio_venta.delete(0, tk.END)
    entryPrecio_venta.insert(tk.END, "$" + str(precio))
    entryTalla_venta.config(state="readonly")
    entryPrecio_venta.config(state="readonly")

def actualizar_reembolso(*args):
    for i in datosCargados:
        if comboboxProducto_reembolso.get() == i.getProducto():
            talla = i.getTalla()
            precio = float(i.getPrecio()) * float(SpinboxCantidad_reembolso.get())
    entryTalla_reembolso.config(state="normal")
    entryPrecio_reembolso.config(state="normal")
    entryTalla_reembolso.delete(0, tk.END)
    entryTalla_reembolso.insert(tk.END, talla)
    entryPrecio_reembolso.delete(0, tk.END)
    entryPrecio_reembolso.insert(tk.END, "$" + str(precio))
    entryTalla_reembolso.config(state="readonly")
    entryPrecio_reembolso.config(state="readonly")

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
                messagebox.showinfo("Producto Vendido", "El producto fue vendido con exito\nProducto: " + i.getProducto() + "\nTalla: " + i.getTalla() + "\nPrecio: " + preciopedido + "\nStock: " + str(i.getStock()) + "\nVentas: " + str(i.getVendido()) + "\nReembolsados: " + str(i.getReembolso()))
                mensaje = "\n----------\nEl producto fue vendido con exito\nProducto: " + i.getProducto() + "\nTalla: " + i.getTalla() + "\nPrecio: " + str(preciopedido) + "\nStock: " + str(i.getStock()) + "\nVentas: " + str(i.getVendido()) + "\nReembolsados: " + str(i.getReembolso()) + "\n----------"
    with open("Ventas.txt", "+a") as venta:
        venta.write(mensaje)

def reembolso(nombrepedido, tallapedido, cantidadpedido, preciopedido):
    for i in datosCargados:
        if i.getProducto() == nombrepedido:
            if i.getTalla() == tallapedido:
                i.setReembolso(int(cantidadpedido))
                messagebox.showinfo("Producto Reembolsado", "El producto fue reembolsado con exito\nProducto: " + i.getProducto() + "\nTalla: " + i.getTalla() + "\nPrecio: " + preciopedido + "\nStock: " + str(i.getStock()) + "\nVentas: " + str(i.getVendido()) + "\nReembolsados: " + str(i.getReembolso()))
                mensaje = "\n----------\nEl producto fue vendido con exito\nProducto: " + i.getProducto() + "\nTalla: " + i.getTalla() + "\nPrecio: " + str(preciopedido) + "\nStock: " + str(i.getStock()) + "\nVentas: " + str(i.getVendido()) + "\nReembolsados: " + str(i.getReembolso()) +"\n----------"
    with open("Reembolsos.txt", "+a") as venta:
        venta.write(mensaje)

def agregarProducto():
    productoagregado = AgregarProducto.main(datosCargados)

def prueba():
    pass

def main():
    #region principal
    global datosCargados, entryTalla_venta, comboboxProducto_venta, entryPrecio_venta, SpinboxCantidad_venta
    global entryTalla_reembolso, comboboxProducto_reembolso, entryPrecio_reembolso, SpinboxCantidad_reembolso
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
    frameProducto_venta = ttk.Frame(tab2)
    frameProducto_venta.pack(anchor="w", pady=5)

    frameTalla_venta = ttk.Frame(tab2)
    frameTalla_venta.pack(anchor="w", pady=5)

    frameCantidad_venta = ttk.Frame(tab2)
    frameCantidad_venta.pack(anchor="w", pady=5)

    framePrecio_venta = ttk.Frame(tab2)
    framePrecio_venta.pack(anchor="w", pady=5)

    labelProducto_venta = tk.Label(frameProducto_venta, text="Producto: ")
    labelProducto_venta.pack(side="left")

    labelTalla_venta = tk.Label(frameTalla_venta, text="Talla: ")
    labelTalla_venta.pack(side="left")

    labelCantidad_venta = tk.Label(frameCantidad_venta, text="Cantidad: ")
    labelCantidad_venta.pack(side="left")

    labelPrecio_venta = tk.Label(framePrecio_venta, text="Precio: ")
    labelPrecio_venta.pack(side="left")

    entryTalla_venta = tk.Entry(frameTalla_venta)
    entryTalla_venta.insert(tk.END, "Talle")
    entryTalla_venta.config(state="readonly")
    entryTalla_venta.pack(side="right")

    comboboxProducto_venta = ttk.Combobox(frameProducto_venta, values=buscarNombres(), state="readonly")
    comboboxProducto_venta.set("Productos")
    comboboxProducto_venta.bind("<<ComboboxSelected>>", actualizar_venta)
    comboboxProducto_venta.pack(side="right")

    SpinboxCantidad_venta = tk.Spinbox(frameCantidad_venta, from_=1, to=100, state="readonly")
    SpinboxCantidad_venta.bind("<<FocusOut>>", actualizar_venta)
    SpinboxCantidad_venta.pack(side="right")

    entryPrecio_venta = tk.Entry(framePrecio_venta, state="readonly")
    entryPrecio_venta.pack(side="right")

    botonVender_venta = tk.Button(tab2, text="Vender", command= lambda: venta(comboboxProducto_venta.get(), entryTalla_venta.get(), SpinboxCantidad_venta.get(), entryPrecio_venta.get()))
    botonVender_venta.pack()
    #endregion

    #region Reembolsos
    frameProducto_reembolso = ttk.Frame(tab3)
    frameProducto_reembolso.pack(anchor="w", pady=5)

    frameTalla_reembolso = ttk.Frame(tab3)
    frameTalla_reembolso.pack(anchor="w", pady=5)

    frameCantidad_reembolso = ttk.Frame(tab3)
    frameCantidad_reembolso.pack(anchor="w", pady=5)

    framePrecio_reembolso = ttk.Frame(tab3)
    framePrecio_reembolso.pack(anchor="w", pady=5)

    labelProducto_reembolso = tk.Label(frameProducto_reembolso, text="Producto: ")
    labelProducto_reembolso.pack(side="left")

    labelTalla_reembolso = tk.Label(frameTalla_reembolso, text="Talla: ")
    labelTalla_reembolso.pack(side="left")

    labelCantidad_reembolso = tk.Label(frameCantidad_reembolso, text="Cantidad: ")
    labelCantidad_reembolso.pack(side="left")

    labelPrecio_reembolso = tk.Label(framePrecio_reembolso, text="Precio: ")
    labelPrecio_reembolso.pack(side="left")

    entryTalla_reembolso = tk.Entry(frameTalla_reembolso)
    entryTalla_reembolso.insert(tk.END, "Talle")
    entryTalla_reembolso.config(state="readonly")
    entryTalla_reembolso.pack(side="right")

    comboboxProducto_reembolso = ttk.Combobox(frameProducto_reembolso, values=buscarNombres(), state="readonly")
    comboboxProducto_reembolso.set("Productos")
    comboboxProducto_reembolso.bind("<<ComboboxSelected>>", actualizar_reembolso)
    comboboxProducto_reembolso.pack(side="right")

    SpinboxCantidad_reembolso = tk.Spinbox(frameCantidad_reembolso, from_=1, to=100, state="readonly")
    SpinboxCantidad_reembolso.bind("<<FocusOut>>", actualizar_reembolso)
    SpinboxCantidad_reembolso.pack(side="right")

    entryPrecio_reembolso = tk.Entry(framePrecio_reembolso, state="readonly")
    entryPrecio_reembolso.pack(side="right")

    botonVender_reembolso = tk.Button(tab3, text="Reembolsar", command= lambda: reembolso(comboboxProducto_reembolso.get(), entryTalla_reembolso.get(), SpinboxCantidad_reembolso.get(), entryPrecio_reembolso.get()))
    botonVender_reembolso.pack()
    #endregion

    notebook.pack(expand=True, fill='both')

    root.mainloop()
    
if __name__ == "__main__":
    main()
