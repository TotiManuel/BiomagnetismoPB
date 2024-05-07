def main():
    with open ("Productos.txt") as Productos:
        totalProductos = []
        productoTupla = Productos.readlines()
        for i in productoTupla:
            producto = i.strip().split(",")
            if producto[0].lower() != "producto":
                agregarProducto = (producto[0], producto[1], producto[2], producto[3])
                totalProductos.append(agregarProducto)
        return totalProductos
if __name__=="__main__":
    main()