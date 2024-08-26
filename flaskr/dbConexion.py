import sqlite3

import click
from flask import current_app, g


"""def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(
            current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row

    return g.db


def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()"""

def agregar_producto(marca, modelo, precio, imagen, descripcion, stock):
    conn = sqlite3.connect('flaskr/KibaStore.db')
    cursor = conn.cursor()
    cursor.execute(
        'INSERT INTO productos (marca, modelo, precio, imagen, descripcion, stock) VALUES (?, ?, ?, ?, ?, ?)',
        (marca, modelo, precio, imagen, descripcion, stock)
    )
    conn.commit()
    conn.close()

agregar_producto(marca="Samsung", modelo="Galaxy", precio=125, imagen=None, descripcion="Perfecto", stock=10)

def eliminar_producto(id_producto):
    conn = sqlite3.connect('flaskr/KibaStore.db')
    cursor = conn.cursor()
    cursor.execute(
        'DELETE FROM productos WHERE id_producto = ?',
        (id_producto,)
    )
    conn.commit()
    conn.close()

# Area de Registro
def registrar_cliente(usuario, contraseña, rol):
    conn = sqlite3.connect('flaskr/KibaStore.db')
    cursor = conn.cursor()
    cursor.execute(
        'INSERT INTO cuentas (usuario, contraseña, rol) VALUES (?, ?, ?)',
        (usuario, contraseña, rol)
         #el rol = 1 es cliente y rol = 2 es admin
    )
    conn.commit()
    conn.close()

# eliminar_producto() #Inserte el fokin id del producto en la funcion

