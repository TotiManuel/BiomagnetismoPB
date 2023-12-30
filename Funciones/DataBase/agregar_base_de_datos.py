import sqlite3
import os.path as path

def agregar_database():
    if path.exists("base_datos_biomagnetismo.db"):
        messagebox.showerror("EXISTE", "Base de datos ya existe.")
    else:
    # Conectar a la base de datos (o crearla si no existe)
        conn = sqlite3.connect('../../base_datos_biomagnetismo.db')
    # Crear un cursor para interactuar con la base de datos
        cursor = conn.cursor()
    # Crear una tabla en la base de datos
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS Productos (
        id INTEGER PRIMARY KEY,
        bool INTEGER,
        producto TEXT,
        valor REAL,
        stock INTEGER,
        ventas INTEGER,
        reembolsos INTEGER,
        talle TEXT
        )
        ''')
    # Ejecutar la sentencia SQL para insertar el nuevo producto
        cursor.execute('INSERT INTO Productos (bool, producto, valor, stock, ventas, reembolsos, talle) VALUES (1, "Producto 1", 3, 2, 0, 0, "M")')
    # Guardar los cambios y cerrar la conexión
        conn.commit()
        conn.close()
