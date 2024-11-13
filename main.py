from flask import Flask, render_template
from controller.ConsultaController import ConsultaController

app = Flask(__name__, template_folder="views")


app.register_blueprint(ConsultaController().blueprint)
@app.get("/login")
def index():
    return render_template("login.html")

@app.post("/login")
def login():
    return "teste"


@app.get("/signup")
def signup():
    return render_template("signup.html")

@app.post("/signup")
def signup_action():
    return "Sucesso Cadastro"



if __name__ == '__main__':
    app.run(debug=True)