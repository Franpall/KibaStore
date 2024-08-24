from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    usuario_logeado = True
    productos = [{"nombre":"xiaomi mi 10", "precio":"1000"},{"nombre":"xiaomi retmi 49", "precio":"600"},{"nombre":"poco x5 pro", "precio":"200"}, {"nombre":"xiaomi mi 10", "precio":"1000"},{"nombre":"xiaomi retmi 49", "precio":"600"},{"nombre":"poco x5 pro", "precio":"200"}]
    return render_template('blog/Inicio.html', usuario_logeado=usuario_logeado, productos=productos)

if __name__ == '__main__':
    app.run(debug=True)