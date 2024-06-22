import sqlite3
from tkinter import messagebox

def insertar_usuario(dni, nombres, apellidos, password, direccion, celular, roles):
    try:
        # Conexión a la base de datos
        conn = sqlite3.connect('ABIBLIOTECA.db')
        cursor = conn.cursor()

        # Insertar el usuario
        cursor.execute('''
        INSERT INTO Usuarios (dni, nombres, apellidos, password, direccion, celular, roles)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (dni, nombres, apellidos, password, direccion, celular, roles))

        # Confirmar la transacción
        conn.commit()

        # Cerrar la conexión
        conn.close()

        return True
    except sqlite3.Error as e:
        messagebox.showerror("Error", f"Error al insertar el usuario: {e}")
        return False
# Función para eliminar un usuario de la base de datos
def eliminar_usuario(id_usuario):
    try:
        # Conexión a la base de datos
        conn = sqlite3.connect('ABIBLIOTECA.db')
        cursor = conn.cursor()

        # Eliminar el usuario
        cursor.execute('''
        DELETE FROM Usuarios
        WHERE id_usuario = ?''', (id_usuario,))

        # Confirmar la transacción
        conn.commit()

        # Cerrar la conexión
        conn.close()

        return True
    except sqlite3.Error as e:
        messagebox.showerror("Error", f"Error al eliminar el usuario: {e}")
        return False

# Función para actualizar un usuario en la base de datos
def actualizar_usuario(id_usuario, dni, nombres, apellidos, password, direccion, celular, roles):
    try:
        # Conexión a la base de datos
        conn = sqlite3.connect('ABIBLIOTECA.db')
        cursor = conn.cursor()

        # Actualizar el usuario
        cursor.execute('''
        UPDATE Usuarios
        SET dni = ?, nombres = ?, apellidos = ?, password = ?, direccion = ?, celular = ?, roles = ?
        WHERE id_usuario = ?''', (dni, nombres, apellidos, password, direccion, celular, roles, id_usuario))

        # Confirmar la transacción
        conn.commit()

        # Cerrar la conexión
        conn.close()

        return True
    except sqlite3.Error as e:
        messagebox.showerror("Error", f"Error al actualizar el usuario: {e}")
        return False

