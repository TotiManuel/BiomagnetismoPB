#region Programa
#region Importaciones
import tkinter as tk
import os
from tkinter import ttk, messagebox
from datetime import datetime, date
#endregion

#region Funciones
def faltaProgramar():
    pass
def calcular_edad(fecha_nacimiento):
    fecha_actual = datetime.now()
    fecha_nacimiento = datetime.strptime(fecha_nacimiento, "%d/%m/%Y")
    edad = fecha_actual.year - fecha_nacimiento.year - ((fecha_actual.month, fecha_actual.day) < (fecha_nacimiento.month, fecha_nacimiento.day))
    return edad
def agregar_turno():
    apellido = apellido_entry.get()
    nombre = nombre_entry.get()
    dni = dni_entry.get()
    fecha_nacimiento = fecha_nacimiento_entry.get()
    monto_consulta = monto_consulta_entry.get()
    servicio = servicio_entry.get()
    fecha_turno = fecha_turno_entry.get()
    hora_turno = hora_turno_entry.get()

    edad = calcular_edad(fecha_nacimiento)

    # Comprobamos que todos los campos estén completos
    if apellido == '' or nombre == '' or dni == '' or fecha_nacimiento == '' or monto_consulta == '' or servicio == '' or fecha_turno == '' or hora_turno == '':
        messagebox.showerror("Error", "Por favor completa todos los campos.")
        return

    # Abrir el archivo en modo de escritura
    with open("turnos.txt", "a") as file:
        # Escribir los datos del turno en el archivo
        file.write(f"{apellido},{nombre},{dni},{fecha_nacimiento},{edad},{monto_consulta},{servicio},{fecha_turno},{hora_turno},No\n")

    messagebox.showinfo("Éxito", "Turno agregado correctamente.")
    apellido_entry.delete(0, tk.END)
    nombre_entry.delete(0, tk.END)
    dni_entry.delete(0, tk.END)
    fecha_nacimiento_entry.delete(0, tk.END)
    monto_consulta_entry.delete(0, tk.END)
    servicio_entry.delete(0, tk.END)
    fecha_turno_entry.delete(0, tk.END)
    hora_turno_entry.delete(0, tk.END)
    mostrar_turnos()
    mostrar_turnos_all()
def calcular_edad(fecha_nacimiento):
    fecha_actual = datetime.now()
    fecha_nacimiento = datetime.strptime(fecha_nacimiento, "%d/%m/%Y")
    edad = fecha_actual.year - fecha_nacimiento.year - ((fecha_actual.month, fecha_actual.day) < (fecha_nacimiento.month, fecha_nacimiento.day))
    return edad
def desmarcar_asistido(index):
    with open("turnos.txt", "r") as file:
        lines = file.readlines()

    # Modificar la línea correspondiente para marcar el turno como asistido
    lines[index] = lines[index].replace("Sí", "No")

    # Escribir todas las líneas modificadas de vuelta al archivo
    with open("turnos.txt", "w") as file:
        file.writelines(lines)

    # Actualizar la lista de turnos
    mostrar_turnos()
    mostrar_turnos_all()
def marcar_asistido(index):
    with open("turnos.txt", "r") as file:
        lines = file.readlines()

    # Modificar la línea correspondiente para marcar el turno como asistido
    lines[index] = lines[index].replace("No", "Sí")

    # Escribir todas las líneas modificadas de vuelta al archivo
    with open("turnos.txt", "w") as file:
        file.writelines(lines)

    # Actualizar la lista de turnos
    mostrar_turnos()
    mostrar_turnos_all()
def borrar_turno(index):
    with open("turnos.txt", "r") as file:
        lines = file.readlines()

    # Eliminar la línea correspondiente al turno
    del lines[index]

    # Escribir todas las líneas actualizadas de vuelta al archivo
    with open("turnos.txt", "w") as file:
        file.writelines(lines)

    # Actualizar la lista de turnos
    mostrar_turnos()
    mostrar_turnos_all()
def mostrar_turnos_all():
    # Limpiar la lista de turnos antes de volver a mostrarla
    for widget in turnos_frame_all.winfo_children():
        widget.destroy()

    if not os.path.exists("turnos.txt"):
        with open("turnos.txt","w") as file:
            file.write("APELLIDO, NOMBRE, DNI, FECHA DE NACIMIENTO, EDAD, MONTOCONSULTA, SERVICIO, FECHA DEL TURNO, HORA DEL TURNO, ASISTIDO\n")

    with open("turnos.txt", "r") as file:
        turnos = file.readlines()

    for i, turno in enumerate(turnos):
        # Saltar la primera línea que contiene los encabezados
        if i == 0:
            continue
        campos = turno.strip().split(",")
        # Crear una cadena formateada para mostrar el turno
        mensaje = f"Paciente: {campos[0]} {campos[1]} - {campos[2]} - {campos[4]} Años - ${campos[5]} - Servicio: {campos[6]} - {campos[7]} - {campos[8]} - Asistido: {campos[9]}\n" + "="*100
        # Crear una etiqueta para mostrar el turno
        turno_label = tk.Label(turnos_frame_all, text=mensaje, padx=10, pady=5)
        turno_label.grid(row=i, column=0, sticky="w")
        if campos[9] == "No":
            pass
        else:
            turno_label.config(background="green")
def mostrar_turnos():
    # Limpiar la lista de turnos antes de volver a mostrarla
    for widget in turnos_frame.winfo_children():
        widget.destroy()

    if not os.path.exists("turnos.txt"):
        with open("turnos.txt","w") as file:
            file.write("APELLIDO, NOMBRE, DNI, FECHA DE NACIMIENTO, EDAD, MONTOCONSULTA, SERVICIO, FECHA DEL TURNO, HORA DEL TURNO, ASISTIDO\n")

    with open("turnos.txt", "r") as file:
        turnos = file.readlines()

    for i, turno in enumerate(turnos):
        # Saltar la primera línea que contiene los encabezados
        if i == 0:
            continue

        # Dividir los campos del turno por las comas
        campos = turno.strip().split(",")
        fecha_actual = date.today()

        if str(campos[7]) == fecha_actual.strftime("%d/%m/%Y"):
            # Crear una cadena formateada para mostrar el turno
            mensaje = f"Paciente: {campos[0]} {campos[1]} - {campos[2]} - {campos[4]} Años - ${campos[5]} - Servicio: {campos[6]} - {campos[7]} - {campos[8]} - Asistido: {campos[9]}"
            # Crear una etiqueta para mostrar el turno
            turno_label = tk.Label(turnos_frame, text=mensaje, padx=10, pady=5)
            turno_label.grid(row=i, column=0, sticky="w")
        else:
            continue
        # Si el turno no ha sido asistido, agregar un botón para marcarlo como asistido
        if campos[9] == "No":
            asistir_button = tk.Button(turnos_frame, text="Asistir", command=lambda i=i: marcar_asistido(i))
            asistir_button.grid(row=i, column=1)
            eliminar_button = tk.Button(turnos_frame, text="Eliminar", command=lambda i=i: borrar_turno(i))
            eliminar_button.grid(row=i, column=2)
        else:
            turno_label.config(background="green")
            cancelar_button = tk.Button(turnos_frame, text="Cancelar", command=lambda i=i: desmarcar_asistido(i))
            cancelar_button.grid(row=i, column=1)

#endregion
def turnero():
    global apellido_entry, nombre_entry, dni_entry, fecha_nacimiento_entry, monto_consulta_entry, servicio_entry, fecha_turno_entry, hora_turno_entry, turnos_frame, turnos_frame_all
    #region principal
    root = tk.Tk()
    root.title("BioMagnetismo")
    
    barraMenu = tk.Menu(root)
    menuArchivo = tk.Menu(barraMenu, tearoff=0)
    menuTurnero = tk.Menu(barraMenu, tearoff=0)

    menuArchivo.add_command(label="Guardar", command=lambda: faltaProgramar(), background="red")
    menuArchivo.add_separator()
    menuArchivo.add_command(label="Salir", command=lambda: root.destroy())
    barraMenu.add_cascade(label="Archivo", menu = menuArchivo)

    menuTurnero.add_command(label="Buscar Paciente", command=lambda: faltaProgramar(), background="red")
    menuTurnero.add_command(label="Turnero", command=lambda: faltaProgramar(), background="red")
    barraMenu.add_cascade(label="Turnero", menu = menuTurnero)
    
    root.config(menu=barraMenu)

    notebook = ttk.Notebook(root)

    tab1 = ttk.Frame(notebook)
    tab2 = ttk.Frame(notebook)
    tab3 = ttk.Frame(notebook)
    tab4 = ttk.Frame(notebook)
    tab5 = ttk.Frame(notebook)

    notebook.add(tab1, text="Agregar Turno")
    notebook.add(tab2, text="Turnos de Hoy")
    notebook.add(tab3, text="Todos los turnos")
    notebook.add(tab4, text="Modificar Turno")
    notebook.add(tab5, text="Agregar Stock")

    #endregion

    #region Agregar Turno
    # Crear los elementos de la interfaz
    apellido_label = tk.Label(tab1, text="Apellido:")
    apellido_label.grid(row=0, column=0, sticky="w")
    apellido_entry = tk.Entry(tab1)
    apellido_entry.grid(row=0, column=1)

    nombre_label = tk.Label(tab1, text="Nombre:")
    nombre_label.grid(row=1, column=0, sticky="w")
    nombre_entry = tk.Entry(tab1)
    nombre_entry.grid(row=1, column=1)

    dni_label = tk.Label(tab1, text="DNI:")
    dni_label.grid(row=2, column=0, sticky="w")
    dni_entry = tk.Entry(tab1)
    dni_entry.grid(row=2, column=1)

    fecha_nacimiento_label = tk.Label(tab1, text="Fecha de Nacimiento (dd/mm/aaaa):")
    fecha_nacimiento_label.grid(row=3, column=0, sticky="w")
    fecha_nacimiento_entry = tk.Entry(tab1)
    fecha_nacimiento_entry.grid(row=3, column=1)

    monto_consulta_label = tk.Label(tab1, text="Monto de la Consulta:")
    monto_consulta_label.grid(row=4, column=0, sticky="w")
    monto_consulta_entry = tk.Entry(tab1)
    monto_consulta_entry.grid(row=4, column=1)

    servicio_label = tk.Label(tab1, text="Servicio en la Consulta:")
    servicio_label.grid(row=5, column=0, sticky="w")
    servicio_entry = tk.Entry(tab1)
    servicio_entry.grid(row=5, column=1)

    fecha_turno_label = tk.Label(tab1, text="Fecha del Turno:")
    fecha_turno_label.grid(row=6, column=0, sticky="w")
    fecha_turno_entry = tk.Entry(tab1)
    fecha_turno_entry.grid(row=6, column=1)

    hora_turno_label = tk.Label(tab1, text="Hora del Turno:")
    hora_turno_label.grid(row=7, column=0, sticky="w")
    hora_turno_entry = tk.Entry(tab1)
    hora_turno_entry.grid(row=7, column=1)

    agregar_button = tk.Button(tab1, text="Agregar Turno", command=agregar_turno)
    agregar_button.grid(row=8, column=0, columnspan=2)
    #endregion

    #region Ventas
    turnos_frame = tk.Frame(tab2)
    turnos_frame.pack(expand=True, fill='both')
    mostrar_turnos()
    #endregion

    #region Reembolsos
    turnos_frame_all = ttk.Frame(tab3)
    turnos_frame_all.pack(anchor="w", pady=5)
    mostrar_turnos_all()
    #endregion

    #region Productos
    frameProductoAgregar = ttk.Frame(tab4)
    frameProductoAgregar.pack(anchor="w", pady=5)

    #endregion

    #region AgregarStock
    frameProducto_Stock = ttk.Frame(tab5)
    frameProducto_Stock.pack(anchor="w", pady=5)

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




