from flask import Blueprint, render_template, redirect, request
from model.Consulta import instance as consulta

class ConsultaController:
    blueprint = Blueprint("Consultas", __name__)
    
    @blueprint.get("/consultas")
    def get():
        data = consulta.get()
        return render_template("home.html", context=data)
    
    @blueprint.post("/consultas")
    def create():
        data = request.form
       # __consulta.create(data)
        
        return redirect("/consultas")