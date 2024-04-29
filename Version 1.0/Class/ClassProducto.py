class Producto:
    def __init__(self, PRODUCTO, PRECIO, TALLA, STOCK, VENDIDO, REEMBOLSO):
        self.PRODUCTO = PRODUCTO
        self.PRECIO = PRECIO
        self.TALLA = TALLA
        self.STOCK = int(STOCK)
        self.VENDIDO = int(VENDIDO)
        self.REEMBOLSO = int(REEMBOLSO)
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
        self.STOCK = self.STOCK + int(newStock)
    def getVendido(self):
        return self.VENDIDO
    def setVendido(self, cantidad):
        self.VENDIDO = self.VENDIDO + cantidad
        self.setStock(self.STOCK - cantidad)
    def setReembolso(self, cantidad):
        self.REEMBOLSO = self.REEMBOLSO + cantidad
        self.STOCK = self.STOCK + cantidad
    def getReembolso(self):
        return self.REEMBOLSO
    def __str__(self):
        print("Clase Producto")
def main():
    pass
if __name__=="__main__":
    main()