from flask import Blueprint, render_template, redirect, request
from model.Consulta import instance as consulta
from model.Medico import instance as medico

class ConsultaController:
    blueprint = Blueprint("Consultas", __name__)
    
    @blueprint.get("/consultas")
    def get():
        data = consulta.get()
        medicos = medico.get()
        return render_template("home.html", consultas=data, medicos=medicos)
    
    @blueprint.post("/consultas")
    def create():
        data = request.form
        
        consulta.create(data)
        
        return redirect("/consultas")