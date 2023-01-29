

from flask import FLask, render_templates

app=Flask(__name__)

@app.route("/")
def index():
    nombre="Juanito"
    lista1=["Español","Inglés","Quimica"]
    return render_templates("index.html,nombre=nombre,lista1=lista1")

@app.route("/usuarios")
def usuarios():
    return render_templates("archivo2.html")

if  __name__=="main":
    app.run(debug=True)