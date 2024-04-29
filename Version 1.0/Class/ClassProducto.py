class Producto:
    def __init__(self, PRODUCTO, PRECIO, TALLA, STOCK):
        self.PRODUCTO = PRODUCTO
        self.PRECIO = PRECIO
        self.TALLA = TALLA
        self.STOCK = int(STOCK)
        self.VENDIDO = 0
        self.REEMBOLSO = 0
    def getProducto(self):
        return self.PRODUCTO
    def setProducto(self, newName):
        self.PRODUCTO = newName
    def getPrecio(self):
        return self.PRECIO
    def setPrecio(self, newPrice):
        self.PRECIO = newPrice
    def getTalla(self):
        return self.TALLA
    def setTalla(self, newTalla):
        self.TALLA = newTalla
    def getStock(self):
        return self.STOCK
    def setStock(self, newStock):
        self.STOCK = newStock
    def getVendido(self):
        return self.VENDIDO
    def setVendido(self, cantidad):
        self.VENDIDO = self.VENDIDO + cantidad
        self.setStock(self.STOCK - cantidad)
    def setReembolso(self, cantidad):
        self.REEMBOLSO = self.REEMBOLSO + cantidad
        self.STOCK = self.STOCK + cantidad
def main():
    pass
if __name__=="__main__":
    main()