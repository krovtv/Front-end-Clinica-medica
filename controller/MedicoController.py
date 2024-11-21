from flask import Blueprint, render_template, session, abort, request, redirect, flash
from model.Consulta import instance as consulta
from model.Exames import instance as exame
from model.TipoExame import instance as tipo_exame
from model.Paciente import instance as paciente

class Medico:
    blueprint = Blueprint("Médico", __name__)
    
    @blueprint.before_request
    def verify_user():
        user = session.get('user')
        if not user or user['tipo'] != 'medico':
            return abort(404)
    
    @blueprint.get("/medico")
    def home():
        user = session.get('user')
        
        consultas = consulta.get_by_medico(user.get('id'))
        return render_template('medico/home.html', consultas=consultas)
    
    @blueprint.get("/medico/exames")
    def get_exames():
        exames = exame.get()
        return render_template('medico/exames.html', exames=exames)
    
    @blueprint.get("/medico/exames/criar")
    def create_exames():
        tipo = tipo_exame.get()
        return render_template('medico/criar_exames.html', tipo_exames=tipo)
    @blueprint.post("/medico/exames/criar")
    def create_exames_action():
        paciente_cpf  = request.form['paciente_cpf']
        data = {
            'data_entrega': request.form['data_entrega'],
            'tipo_exame': request.form['tipo_exame'],
        }
        
        id_paciente = paciente.get_by_cpf(paciente_cpf)[0]
        data['id_paciente'] = id_paciente
        
        
        exame.create(data)
        flash('Exame criado com sucesso')
    
            
        
        return redirect("/medico/exames")