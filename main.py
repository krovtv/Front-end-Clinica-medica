from flask import Flask, render_template
from controller.ConsultaController import ConsultaController
from datetime import datetime

app = Flask(__name__, template_folder="views")


app.register_blueprint(ConsultaController().blueprint)

@app.template_filter()
def format_date(value: str):
    return datetime.fromisoformat(value).strftime("%d/%m/%Y")
@app.template_filter()
def format_hour(value: str):
    return datetime.fromisoformat(value).strftime("%H:%M")

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