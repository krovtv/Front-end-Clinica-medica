from flask import Blueprint, render_template, session, abort
from model.Consulta import instance as consulta

class Medico:
    blueprint = Blueprint("Médico", __name__)
    
    @blueprint.get("/medico")
    def home():
        user = session.get('user')
        if not user or user['tipo'] != 'medico':
            return abort(404)
        
        consultas = consulta.get_by_medico(user.get('id'))
        return render_template('medico/home.html', consultas=consultas)