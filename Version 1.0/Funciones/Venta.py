from Class.ClassProducto import Producto
def main(datosCargados, nombrepedido, preciopedido, tallapedido):
    for i in datosCargados:
        if i[0] == nombrepedido:
            if float(i[1]) == float(preciopedido):
                if i[2] == tallapedido:
                    productocreado = Producto(i[0], i[1], i[2], i[3])
                    productocreado.setVendido(1)
                    print("Producto Vendido")
    return(productocreado)
if __name__=="__main__":
    main()