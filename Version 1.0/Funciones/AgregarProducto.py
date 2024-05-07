import tkinter as tk
def cargarNuevoProducto(datosCargados):
    pass
    #newDatosCargados = []
    #for i in datosCargados:
    #    newDatosCargados.append(i)
    #newDatosCargados.append((nombre, precio, talla, stock))
    #print("Producto Cargado")
    #return newDatosCargados
def main(datosCargados):
    root = tk.Tk()
    root.title("Registro Producto")
    root.geometry("400x500+0+0")

    barraMenu = tk.Menu(root)
    menuArchivo = tk.Menu(barraMenu, tearoff=0)

    root.mainloop()    
if __name__=="__main__":
    main()

'''
    
'''