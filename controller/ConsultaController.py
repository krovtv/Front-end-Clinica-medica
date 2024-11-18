from flask import Blueprint, render_template, redirect, request
from model.Consulta import instance as consulta
from model.Medico import instance as medico
from model.Paciente import instance as paciente


class ConsultaController:
    blueprint = Blueprint("Consultas", __name__, url_prefix="/consultas")
    
    @blueprint.get("/")
    def get():
        data = consulta.get()
        medicos = medico.get()

        return render_template("home.html", consultas=data, medicos=medicos)
    
    @blueprint.post("/")
    def create():
        paciente_cpf = request.form["paciente_cpf"]
        data_agendamento = request.form["data_agendamento"]
        id_medico = request.form["medico"]
        
        paciente_pelo_cpf = paciente.get_by_cpf(paciente_cpf)  
        
        data = {
            "id_paciente": paciente_pelo_cpf[0],
            "data_agendamento": data_agendamento,
            "id_medico": id_medico
        }
        
        consulta.create(data)
        
        return redirect("/consultas")
    
    @blueprint.get("/delete/<id>")
    def delete(id):
        consulta.delete(id)
        return redirect("/consultas")