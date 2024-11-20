from flask import Blueprint, render_template, request, redirect
from model.Especialidade import instance as especialidade
from model.Medico import instance as medico
from model.Funcionario import instance as funcionario

class Cadastro:
    blueprint = Blueprint("Cadastro", __name__)
    
    @blueprint.get("/medico/cadastro")
    def signup_medico():
        especialidades = especialidade.get()
        
        return render_template("medico/cadastrar.html", especialidades=especialidades)
    
    
    @blueprint.post("/medico/cadastro")
    def signup_medico_action():
        data = {
            'email': request.form['email'],
            'senha': request.form['senha'],
            'data_nascimento': request.form['data_nascimento'],
            'idade': request.form['idade'],
            'especialidade': request.form['especialidade'],
            'nome': request.form['nome'],
        }
        
        try:
            medico.register(data['email'],  data['senha'], data['nome'], data['data_nascimento'], data['idade'])
            return redirect('/medico/login')
        except:
            return redirect('/medico/cadastro')
    
    
    @blueprint.get("/funcionario/cadastro")
    def signup_funcionario():
        return render_template('/funcionario/cadastrar.html')
    
    @blueprint.post("/funcionario/cadastro")
    def signup_funcionario_action():
        data = {
            'email': request.form['email'],
            'senha': request.form['senha'],
            'data_nascimento': request.form['data_nascimento'],
            'idade': request.form['idade'],
            'cargo': request.form['cargo'],
            'nome': request.form['nome']
        }
        try:
            funcionario.create(data)
            return redirect("/funcionario/login")
        except:
            return redirect("/funcionario/cadastro")