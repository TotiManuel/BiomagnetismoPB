def main(datosCargados, nombre, precio, talla, stock):
    newDatosCargados = []
    for i in datosCargados:
        newDatosCargados.append(i)
    newDatosCargados.append((nombre, precio, talla, stock))
    print("Producto Cargado")
    return newDatosCargados
if __name__=="__main__":
    main()