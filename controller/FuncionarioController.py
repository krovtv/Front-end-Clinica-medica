from sqlite3 import IntegrityError
from flask import Blueprint, session, abort, render_template, request, flash, redirect
from model.Paciente import instance as paciente
from model.Exames import instance as exame

class Funcionario:
    blueprint = Blueprint("Funcionario", __name__, url_prefix="/funcionario")
    
    @blueprint.before_request
    def verify_user():
        user = session.get('user')
        
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
    
    @blueprint.get("/paciente")
    def listar_pacientes():
        pacientes = paciente.get()
        
        return render_template("funcionario/listar_pacientes.html", pacientes=pacientes)
    
    @blueprint.get("/deletar/<id>/paciente")
    def delete_paciente(id):
        paciente.delete(id)
        return redirect("/funcionario/paciente")
    
    @blueprint.get("/atualizar/<id>/paciente")
    def atualizar_paciente(id):
        paciente_escolhido = paciente.get(id)
        return render_template("funcionario/editar_paciente.html", paciente=paciente_escolhido)
    
    @blueprint.post('/atualizar/<id>/paciente')
    def atualizar_paciente_action(id):
        try:
            data = {
                'cpf': request.form['cpf'],
                'idade': request.form['idade'],
                'nome': request.form['nome'],
            }
            
            paciente.update(data, id)
        except Exception as e:
            print(e)
            flash("Houve um erro interno. Tente novamente mais tarde !")
        
        return redirect('/funcionario/paciente')
        
    
    @blueprint.get("/exames")
    def list_exames():
        exames = exame.get()
        return render_template("funcionario/exames.html", exames=exames)
    
    @blueprint.get("/exames/<id>/receber")
    def receber_exame(id):
        exame.alter_recebimento_exame(id, True)
        return redirect('/funcionario/exames')
    
    @blueprint.get("/exames/<id>/cancelar")
    def cancelar_exame(id):
        exame.alter_recebimento_exame(id, False)
        return redirect('/funcionario/exames')