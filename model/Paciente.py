from model.Model import Model
from db import conn, cursor
from sqlite3 import IntegrityError

class Paciente(Model):
    def get_by_cpf(self, cpf: str):
        sql = "SELECT ROWID as id, nome, idade, cpf from pacientes WHERE cpf = ? LIMIT 1;"
        
        cursor.execute(sql, [cpf])
        return cursor.fetchone()
    
    def create(self, data):
        sql = "INSERT INTO pacientes (nome, idade, cpf) VALUES (?, ?, ?)"
        cursor.execute(sql, [data['nome'], data['idade'], data['cpf']])
        conn.commit()
        
        return cursor.lastrowid
        
        
    


instance = Paciente()