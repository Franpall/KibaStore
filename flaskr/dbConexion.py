import sqlite3

def agregar_producto(marca, modelo, precio, imagen, descripcion, stock):
    conn = sqlite3.connect('flaskr/KibaStore.db')
    cursor = conn.cursor()
    cursor.execute(
        'INSERT INTO productos (marca, modelo, precio, imagen, descripcion, stock) VALUES (?, ?, ?, ?, ?, ?)',
        (marca, modelo, precio, imagen, descripcion, stock)
    )
    conn.commit()
    conn.close()

def mostrar_productos():
    conn = sqlite3.connect('flaskr/KibaStore.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM productos ORDER BY precio DESC LIMIT 50')
    productos = cursor.fetchall()
    conn.close()
    return productos

def mostrar_producto(id_producto):
    conn = sqlite3.connect('flaskr/KibaStore.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM productos WHERE id_producto = ?', (id_producto,))
    producto = cursor.fetchone()
    conn.close()
    return producto

def reducir_stock(id_producto):
    conn = sqlite3.connect('flaskr/KibaStore.db')
    cursor = conn.cursor()
    cursor.execute('SELECT stock FROM productos WHERE id_producto=?', (id_producto,))
    stock = cursor.fetchone()
    if stock[0] > 0:
        cursor.execute('UPDATE productos SET stock = stock - 1 WHERE id_producto = ?', (id_producto,))
        conn.commit()
        conn.close()
        return "Se agregó al Carrito :]"
    else:
        return "Alguien compró antes que tú y se agotó :[ "
    

# Area de Login
def iniciar_sesionBD(usuario, contraseña):
    conn = sqlite3.connect('flaskr/KibaStore.db')
    cursor = conn.cursor()
    cursor.execute('SELECT rol FROM cuentas WHERE usuario=? AND contraseña=?', (usuario, contraseña))
    resultado = cursor.fetchone()
    if resultado:
        resultado, = resultado
        return resultado

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