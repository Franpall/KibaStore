from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    usuario_logeado = False
    productos = [{"nombre":"xiaomi mi 10", "precio":"1000","cantidad":"2"},{"nombre":"xiaomi retmi 49", "precio":"600","cantidad":"2"},{"nombre":"poco x5 pro", "precio":"200","cantidad":"2"}, {"nombre":"xiaomi mi 10", "precio":"1000","cantidad":"2"},{"nombre":"xiaomi retmi 49", "precio":"600","cantidad":"2"},{"nombre":"poco x5 pro", "precio":"200","cantidad":"2"}]
    return render_template('blog/Inicio.html', usuario_logeado=usuario_logeado, productos=productos)

@app.route("/carrito")
def cart():
    usuario_logeado = True
    productos = [{"nombre":"xiaomi mi 10", "precio":"1000","cantidad":"2"},{"nombre":"xiaomi retmi 49", "precio":"600","cantidad":"2"},{"nombre":"poco x5 pro", "precio":"200","cantidad":"2"}, {"nombre":"xiaomi mi 10", "precio":"1000","cantidad":"2"},{"nombre":"xiaomi retmi 49", "precio":"600","cantidad":"2"},{"nombre":"poco x5 pro", "precio":"200","cantidad":"2"}]
    return render_template('blog/carrito.html', usuario_logeado=usuario_logeado, items=productos)

@app.route("/login")
def iniciarSesion():
    return render_template('auth/login.html')

if __name__ == '__main__':
    app.run(debug=True)