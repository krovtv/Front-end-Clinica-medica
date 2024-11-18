from flask import Blueprint, render_template, redirect, request
from model.Consulta import instance as consulta
from model.Medico import instance as medico
from model.Paciente import instance as paciente


class ConsultaController:
    blueprint = Blueprint("Consultas", __name__)
    
    @blueprint.get("/consultas")
    def get():
        data = consulta.get()
        medicos = medico.get()

        return render_template("home.html", consultas=data, medicos=medicos)
    
    @blueprint.post("/consultas")
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