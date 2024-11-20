from flask import Flask, render_template, session, redirect

from controller.ConsultaController import ConsultaController
from controller.Login import Login
from controller.Cadastro import Cadastro
from controller.MedicoController import Medico
from controller.FuncionarioController import Funcionario

from datetime import datetime
import os
from dotenv import load_dotenv


# Carrega variavéis de ambiente
load_dotenv()

# Configurações iniciais da aplicação
app = Flask(__name__, template_folder="views")
app.secret_key = os.environ['SECRET_KEY']


@app.template_filter()
def format_date(value: str):
    return datetime.fromisoformat(value).strftime("%d/%m/%Y")
@app.template_filter()
def format_hour(value: str):
    return datetime.fromisoformat(value).strftime("%H:%M")

@app.get("/")
def choose_type_login():
        user = session.get('user')
        if user is None:
            return render_template("choose_type_login.html")
        elif user['tipo'] == 'medico':
            return redirect('/medico')
        
        return redirect("/consultas/")

@app.errorhandler(404)
def not_found_page(_):
    return render_template("utils/404.html"), 404

@app.get("/logout")
def logout():
    session['user'] = None
    return redirect("/")


app.register_blueprint(ConsultaController().blueprint)
app.register_blueprint(Login().blueprint)
app.register_blueprint(Cadastro().blueprint)
app.register_blueprint(Medico().blueprint)
app.register_blueprint(Funcionario().blueprint)



if __name__ == '__main__':
    app.run(debug=True)