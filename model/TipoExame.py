from model.Model import Model
from db import conn, cursor

class TipoExame(Model):
    def get(self):
        sql = "SELECT ROWID AS id, nome, descricao FROM tipo_exame"
        
        cursor.execute(sql)
        return cursor.fetchall()
    

instance = TipoExame()