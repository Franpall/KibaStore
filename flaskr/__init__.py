import os

from flask import Flask, render_template, request
from flaskr.dbConexion import *


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says Hola Insanos :v

    app = Flask(__name__)

    @app.route("/")
    def index(sesion=0):
        productos = [{"nombre":"xiaomi mi 10", "precio":"1000","cantidad":"2"},{"nombre":"xiaomi retmi 49", "precio":"600","cantidad":"2"},{"nombre":"poco x5 pro", "precio":"200","cantidad":"2"}, {"nombre":"xiaomi mi 10", "precio":"1000","cantidad":"2"},{"nombre":"xiaomi retmi 49", "precio":"600","cantidad":"2"},{"nombre":"poco x5 pro", "precio":"200","cantidad":"2"}]
        return render_template('blog/Inicio.html', usuario_logeado=sesion, productos=productos)

    @app.route("/carrito")
    def cart():
        usuario_logeado = True
        productos = [{"nombre":"xiaomi mi 10", "precio":"1000","cantidad":"2"},{"nombre":"xiaomi retmi 49", "precio":"600","cantidad":"2"},{"nombre":"poco x5 pro", "precio":"200","cantidad":"2"}, {"nombre":"xiaomi mi 10", "precio":"1000","cantidad":"2"},{"nombre":"xiaomi retmi 49", "precio":"600","cantidad":"2"},{"nombre":"poco x5 pro", "precio":"200","cantidad":"2"}]
        return render_template('blog/carrito.html', usuario_logeado=usuario_logeado, items=productos)

    @app.route("/login")
    def iniciarSesion():
        return render_template('auth/login.html')
    
    # Lógica para el inicio de sesion

    @app.route("/loginSolicitud", methods=('GET', 'POST'))
    def loginSolicitud():
        print("confirmado")
        if request.method == 'POST':
            usuario = request.form['username']
            contraseña = request.form['password']
            print(usuario, contraseña) #aca están los datos recibidos bro
            resultado = iniciar_sesionBD(usuario, contraseña)
            print(resultado)
            if resultado == 1:
                sesion = True
                return index(sesion)
            elif resultado == 2:
                return formProductos()
            else:
                mensaje = "Usuario o Contraseña Incorrecta!"
                return render_template('auth/login.html', mensaje = mensaje)


    @app.route("/register")
    def registrar():
        return render_template('auth/register.html')
    
    # Lógica para el registro
    @app.route('/registerSolicitud', methods=('GET', 'POST'))
    def registerSolicitud():
        if request.method == 'POST':
            usuario = request.form['username']
            contraseña = request.form['password']
            print(usuario, contraseña) #aca están los datos recibidos bro

            registrar_cliente(usuario, contraseña, 1)
            mensaje = "Cuenta Creada Con Éxito, ahora Inicia Sesión"
            return render_template('auth/login.html', mensaje = mensaje)
        

    @app.route("/productos_admin")
    def formProductos():
        return render_template('blog/productosView.html')
    
    @app.route("/bye")
    def cerrarSesion():
        sesion = False
        return index(sesion)

    if __name__ == '__main__':
        app.run(debug=True)

    return app