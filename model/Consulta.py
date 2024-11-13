from model.Model import Model
from db import conn, cursor

class Consulta(Model):
    def create(self, data):
        sql = "INSERT INTO consulta (data_agendamento, id_paciente, id_medico) VALUES (?,?,?)"
        cursor.execute(sql, [data["data_agendamento"], data["id_paciente"], data["id_medico"]])
        conn.commit()
        
    
    def update(self, data, id):
        sql = "UPDATE consulta SET"
        
        sql += "WHERE id = ?"
    
    def delete(self, id):
        sql = "DELETE FROM consulta WHERE id = ?"
        cursor.execute(sql, [id])
        conn.commit()
        
    def get(self, id: int | None = None):
        sql =  "SELECT * from consultas "
        if id is not None:
            sql += "WHERE id = ?"
        
        cursor.execute(sql)
        data = cursor.fetchall() if id is None else cursor.fetchone()
        
        return data
    

instance = Consulta()