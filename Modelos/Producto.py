class Producto:
    def __init__(self, codigo, nombre, talla, precio):
        self.codigo = codigo
        self.nombre = nombre
        self.talla = talla
        self.precio = precio
    
    def __str__(self):
        return f"{self.codigo},{self.nombre},{self.talla},{self.precio}"