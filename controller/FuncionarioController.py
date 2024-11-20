from sqlite3 import IntegrityError
from flask import Blueprint, session, abort, render_template, request, flash, redirect
from model.Paciente import instance as paciente

class Funcionario:
    blueprint = Blueprint("Funcionario", __name__, url_prefix="/funcionario")
    
    @blueprint.before_request
    def verify_user():
        user = session['user']
        
        if not user or user['tipo'] != 'funcionario':
            return abort(404)
        
    
    @blueprint.get("/criar/paciente")
    def create_paciente():
        return render_template("funcionario/criar_paciente.html")
    
    @blueprint.post("/criar/paciente")
    def create_paciente_action():
        data = {
            'idade': request.form['idade'],
            'nome': request.form['nome'],
            'cpf': request.form['cpf'],
        }
        try:
            paciente.create(data)
            flash('Paciente criado')
        except IntegrityError:
            flash("CPF já cadastrado")
        
        return redirect('/funcionario/criar/paciente')