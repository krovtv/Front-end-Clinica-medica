from flask import Blueprint, render_template


class Login:
    blueprint = Blueprint("Login", __name__)
    
    @blueprint.get("/")
    
    
    
    @blueprint.get("/medico/login")
    def medico_login():
        return render_template("medico/login.html")
    
    @blueprint.post("/medico/login")
    def medico_login_action():
        return render_template("login.html")
    
    @blueprint.get("/funcionario/login")
    def funcionario_login():
        return render_template("funcionario/login.html")
    
    @blueprint.post("/funcionario/login")
    def funcionario_login_action():
        return render_template("login.html")