from model.Model import Model
from db import conn, cursor
from sqlite3 import IntegrityError

class Paciente(Model):
    def get(self, id: int = None):
        sql = "SELECT ROWID as id, nome, idade, cpf from pacientes"
        
        if id is None:    
            cursor.execute(sql)
            return cursor.fetchall()
        
        sql += " WHERE id = ?"
        cursor.execute(sql, [id])
        
        return cursor.fetchone()
    def get_by_cpf(self, cpf: str):
        sql = "SELECT ROWID as id, nome, idade, cpf from pacientes WHERE cpf = ? LIMIT 1;"
        
        cursor.execute(sql, [cpf])
        return cursor.fetchone()
    
    def create(self, data):
        sql = "INSERT INTO pacientes (nome, idade, cpf) VALUES (?, ?, ?)"
        cursor.execute(sql, [data['nome'], data['idade'], data['cpf']])
        conn.commit()
        
        return cursor.lastrowid
    
    def delete(self, id):
        sql = "DELETE FROM pacientes WHERE ROWID = ?"
        cursor.execute(sql, [id])
        conn.commit()
    
    
    def update(self, data, id):
        sql  = "UPDATE pacientes SET nome = ?, idade = ?, cpf = ? WHERE ROWID = ?;"
        
        cursor.execute(sql, [data['nome'], data['idade'], data['cpf'], id])
        conn.commit()
        
        
        
    


instance = Paciente()