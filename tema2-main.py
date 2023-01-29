

from flask import FLask

app=Flask(__name__)

@app.route("/")
def index():
    return "¡¡Hola mundo!!"

@app.route('/hola')
def hola():
    return "<h1> saludo desde Hola </h1>"

@app.route('/nueva')
def nueva():
    return "<h1> saludo desde Nueva </h1>"


if  __name__=="main":
    app.run(debug=True)