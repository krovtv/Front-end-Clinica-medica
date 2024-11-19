from flask import Flask, render_template
from controller.ConsultaController import ConsultaController
from controller.Login import Login
from datetime import datetime

app = Flask(__name__, template_folder="views")

@app.template_filter()
def format_date(value: str):
    return datetime.fromisoformat(value).strftime("%d/%m/%Y")
@app.template_filter()
def format_hour(value: str):
    return datetime.fromisoformat(value).strftime("%H:%M")

@app.get("/")
def choose_type_login():
        return render_template("choose_type_login.html")


app.register_blueprint(ConsultaController().blueprint)
app.register_blueprint(Login().blueprint)



if __name__ == '__main__':
    app.run(debug=True)