

from flask import FLask

app=Flask(__name__)

@app.route("/")
def index():
    return "¡¡Hola mundo!!"

if  __name__=="main":
    app.run(debug=True)