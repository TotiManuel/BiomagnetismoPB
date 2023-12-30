import sqlite3
import os.path as path
def obtener_opciones():
    if path.exists('../../base_datos_biomagnetismo.db'):
        conn = sqlite3.connect('../../base_datos_biomagnetismo.db')
        cursor = conn.cursor()
        #Asegúrate de que la tabla Productos exista en tu base de datos
        cursor.execute('CREATE TABLE IF NOT EXISTS Productos (id INTEGER PRIMARY KEY, producto TEXT, valor INTEGER, stock INTEGER, bool INTEGER DEFAULT 0)')
        conn.commit()
        # Recupera los productos desde la base de datos donde bool es igual a 1
        cursor.execute('SELECT producto FROM Productos WHERE bool = 1')
        productos = [fila[0] for fila in cursor.fetchall()]
        conn.close()
        return productos
    else:
        print("no existe")
'''import sqlite3
def obtener_opciones():
    conn = sqlite3.connect('base_datos_biomagnetismo.db')
    cursor = conn.cursor()

    # Asegúrate de que la tabla Productos exista en tu base de datos
    cursor.execute('CREATE TABLE IF NOT EXISTS Productos (id INTEGER PRIMARY KEY, producto TEXT, valor INTEGER, stock INTEGER)')
    conn.commit()

    # Recupera los productos desde la base de datos
    cursor.execute('SELECT producto FROM Productos')
    productos = [fila[0] for fila in cursor.fetchall()]

    conn.close()
    return productos'''
