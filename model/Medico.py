from model.Model import Model
from db import conn, cursor

class Medico(Model):
    def get(self):
        sql = "SELECT ROWID AS id, nome, idade, especialidade FROM medicos;"
        cursor.execute(sql)
        return cursor.fetchall()
    
    def get_by_id(self, id):
        sql = "SELECT ROWID AS id, nome, idade, especialidade FROM medicos WHERE id = ?;"
        cursor.execute(sql, [id])
        
        return cursor.fetchone()
    
    

instance = Medico()