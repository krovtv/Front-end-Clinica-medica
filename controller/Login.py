from flask import Blueprint, render_template, redirect, request
from model.Medico import instance as medico
from model.Funcionario import instance as funcionario

class Login:
    blueprint = Blueprint("Login", __name__)
    @blueprint.get("/medico/login")
    def medico_login():
        return render_template("medico/login.html")
    
    @blueprint.post("/medico/login")
    def medico_login_action():
        data = {
            'email': request.form["email"],
            'senha': request.form["senha"]
        }
        
        autenticado = medico.authenticate(data['email'],  data['senha'])
        if not autenticado:
            return redirect("/medico/login")
            
        return redirect("/consultas/")
    
    @blueprint.get("/funcionario/login")
    def funcionario_login():
        return render_template("funcionario/login.html")
    
    @blueprint.post("/funcionario/login")
    def funcionario_login_action():
        data = {
            'email': request.form['email'],
            'senha': request.form['senha'],
        }
        
        autorizado = funcionario.authorize(data['email'], data['senha'])
        if not autorizado:
            return redirect('/funcionario/login')
        
        return redirect("/consultas/")