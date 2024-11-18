from model.Model import Model
from db import conn, cursor

class Paciente(Model):
    def get_by_cpf(self, cpf: str):
        sql = "SELECT ROWID as id, nome, idade, cpf from pacientes WHERE cpf = ? LIMIT 1;"
        
        cursor.execute(sql, [cpf])
        return cursor.fetchone()
    


instance = Paciente()