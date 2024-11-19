from model.Model import Model
from db import cursor, conn

class Especialidade(Model):
    def get(self, id = None):
        sql = "SELECT ROWID AS id, nome, descricao FROM especialidades"
        
        if not id:
            cursor.execute(sql)
            return cursor.fetchall()
        
        sql += " WHERE id = ?"
        cursor.execute(sql, [id])
        
        return cursor.fetchone()
    


instance = Especialidade()