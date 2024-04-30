#region Programa
#region Importaciones
from Class.ClassProducto import Producto
import tkinter as tk
from tkinter import ttk, messagebox
import random
from tkinter import PhotoImage
#endregion

#region Funciones
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

def actualizar_pasaje():
    pass

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

def guardarNuevosProductos(nombre, precio, talla, stock, vendido, reembolsado):
    Clase = Producto(nombre, precio, talla, stock, vendido, reembolsado)
    datosCargados.append(Clase)
    with open("Productos.txt", "w") as newProduct:
        newProduct.write("PRODUCTO, PRECIO, TALLA, STOCK, VENTAS, REEMBOLSO")
        for i in datosCargados:
            newProduct.write("\n" + str(i.getProducto()) + "," + str(i.getPrecio()) + "," + str(i.getTalla()) + "," + str(i.getStock()) + "," + str(i.getVendido()) + "," + str(i.getReembolso()))
    messagebox.showinfo("Guardado", "Producto Guardado")

def buscarNombres():
    nombres = []
    for i in datosCargados:
        if int(i.getStock()) > 0:
            nombres.append(i.getProducto())
        else:
            pass
    return(nombres)

def buscarNombresStock():
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

def agregarProducto(nombrepedido, cantidadpedido):
    for i in datosCargados:
        if i.getProducto() == nombrepedido:
            i.setStock(cantidadpedido)
            messagebox.showinfo("Producto Agregado", "El producto fue agregado con exito\nProducto: " + i.getProducto() + "\nStock: " + str(i.getStock()))

def protocoloDeCierre():
    pregunta = messagebox.askyesno("Estas segura?", "Estas segura que deseas cerrar el programa?")
    if pregunta:
        with open("Productos.txt", "w") as newProduct:
            newProduct.write("PRODUCTO, PRECIO, TALLA, STOCK, VENTAS, REEMBOLSO")
            for i in datosCargados:
                newProduct.write("\n" + str(i.getProducto()) + "," + str(i.getPrecio()) + "," + str(i.getTalla()) + "," + str(i.getStock()) + "," + str(i.getVendido()) + "," + str(i.getReembolso()))
        quit()
    else:
        messagebox.showinfo("Sigamos Entonces", "De acuerdo, sigamos trabajando")
#endregion
def turnero():
        #region principal
    global datosCargados, entryTalla_venta, comboboxProducto_venta, entryPrecio_venta, SpinboxCantidad_venta
    global entryTalla_reembolso, comboboxProducto_reembolso, entryPrecio_reembolso, SpinboxCantidad_reembolso
    datosCargados = cargaDatos()
    root = tk.Tk()
    root.title("BioMagnetismo")
    root.protocol("WM_DELETE_WINDOW", protocoloDeCierre)

    barraMenu = tk.Menu(root)
    menuArchivo = tk.Menu(barraMenu, tearoff=0)
    menuTurnero = tk.Menu(barraMenu, tearoff=0)

    menuArchivo.add_command(label="Guardar", command=lambda: guardarNuevosProductos())
    barraMenu.add_cascade(label="Archivo", menu = menuArchivo)

    menuTurnero.add_command(label="Buscar Paciente", command=lambda: quit())
    menuTurnero.add_command(label="Turnero", command=lambda: protocoloDeCierre())
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

    imagen = PhotoImage(file="logo.png").subsample(2, 2)
    label_imagen = tk.Label(tab1, image=imagen)
    label_imagen.pack()
    #endregion

    #region Bienvenido
    mensajes = ["Yo y Jehova siempre creimos en ustedes!", "Hoy es un dia perfecto para ser feliz!", "Si tuviste un mal dia, recordá que Jesus soportó cosas peores!"]
    pasajeAleatorio = random.randint(0,1)

    frameProducto_bienvenido = ttk.Frame(tab1)
    frameProducto_bienvenido.pack(anchor="w", pady=5)

    labelProducto_bienvenido = tk.Label(frameProducto_bienvenido, text=mensajes[pasajeAleatorio])
    labelProducto_bienvenido.pack(side="left")
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

    #region Productos
    frameProductoAgregar = ttk.Frame(tab4)
    frameProductoAgregar.pack(anchor="w", pady=5)

    frameTallaProductoAgregar = ttk.Frame(tab4)
    frameTallaProductoAgregar.pack(anchor="w", pady=5)

    frameCantidadProductoAgregar = ttk.Frame(tab4)
    frameCantidadProductoAgregar.pack(anchor="w", pady=5)

    framePrecioProductoAgregar = ttk.Frame(tab4)
    framePrecioProductoAgregar.pack(anchor="w", pady=5)

    labelProductoProductoAgregar = tk.Label(frameProductoAgregar, text="Producto: ")
    labelProductoProductoAgregar.pack(side="left")

    labelTallaProductoAgregar = tk.Label(frameTallaProductoAgregar, text="Talla: ")
    labelTallaProductoAgregar.pack(side="left")

    labelCantidadProductoAgregar = tk.Label(frameCantidadProductoAgregar, text="Cantidad: ")
    labelCantidadProductoAgregar.pack(side="left")

    labelPrecioProductoAgregar = tk.Label(framePrecioProductoAgregar, text="Precio: ")
    labelPrecioProductoAgregar.pack(side="left")

    entryTallaProductoAgregar = tk.Entry(frameTallaProductoAgregar)
    entryTallaProductoAgregar.pack(side="right")

    entryProductoAgregar = ttk.Entry(frameProductoAgregar, state="normal")
    entryProductoAgregar.pack(side="right")

    SpinboxCantidadProductoAgregar = tk.Spinbox(frameCantidadProductoAgregar, from_=1, to=100)
    SpinboxCantidadProductoAgregar.bind("<<FocusOut>>", actualizar_reembolso)
    SpinboxCantidadProductoAgregar.pack(side="right")

    entryPrecioProductoAgregar = tk.Entry(framePrecioProductoAgregar)
    entryPrecioProductoAgregar.pack(side="right")

    botonVenderProductoAgregar = tk.Button(tab4, text="Agregar", command= lambda: guardarNuevosProductos(entryProductoAgregar.get(), entryPrecioProductoAgregar.get(), entryTallaProductoAgregar.get(), SpinboxCantidadProductoAgregar.get(), 0, 0))
    botonVenderProductoAgregar.pack()                                                                     
    #endregion

    #region AgregarStock
    frameProducto_Stock = ttk.Frame(tab5)
    frameProducto_Stock.pack(anchor="w", pady=5)

    frameCantidad_Stock = ttk.Frame(tab5)
    frameCantidad_Stock.pack(anchor="w", pady=5)

    labelProducto_Stock = tk.Label(frameProducto_Stock, text="Producto: ")
    labelProducto_Stock.pack(side="left")

    labelCantidad_Stock = tk.Label(frameCantidad_Stock, text="Cantidad: ")
    labelCantidad_Stock.pack(side="left")

    comboboxProducto_Stock = ttk.Combobox(frameProducto_Stock, values=buscarNombresStock(), state="readonly")
    comboboxProducto_Stock.set("Productos")
    comboboxProducto_Stock.bind("<<ComboboxSelected>>")
    comboboxProducto_Stock.pack(side="right")

    SpinboxCantidad_Stock = tk.Spinbox(frameCantidad_Stock, from_=1, to=100, state="readonly")
    SpinboxCantidad_Stock.bind("<<FocusOut>>")
    SpinboxCantidad_Stock.pack(side="right")

    botonAgregarStock = tk.Button(tab5, text="Agregar", command= lambda: agregarProducto(comboboxProducto_Stock.get(), SpinboxCantidad_Stock.get()))
    botonAgregarStock.pack()
    #endregion

    notebook.pack(expand=True, fill='both')

    root.mainloop()
#endregion
#region Main
def main():
    turnero()    

if __name__ == "__main__":
    main()
#endregion