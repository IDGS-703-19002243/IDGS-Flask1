

from flask import FLask

app=Flask(__name__)

@app.route("user/<string:user>")
def user(user):
    return "¡¡Hola mundo!! " + user


@app.route("numero/<int:n>")
def numero(n):
    return "Numero: {}".format(n)


@app.route("user/<int:id>/<string:name>")
def func(id,name):
    return "ID: {} Nombre: {}".format(id,name)


@app.route("suma/<float:n1>/<float:n2>")
def suma(n1,n2):
    return "La suma es: {}".format(n1+n2)

if  __name__=="main":
    app.run(debug=True)