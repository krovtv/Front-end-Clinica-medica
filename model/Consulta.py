from model.Model import Model
from db import conn, cursor

class Consulta(Model):
    def create(self, data):
        sql = "INSERT INTO consultas (data_agendamento, id_paciente, id_medico) VALUES (?,?,?)"
        cursor.execute(sql, [data["data_agendamento"], data["id_paciente"], data["id_medico"]])
        conn.commit()
        
    
    def update(self, data, id):
        sql = "UPDATE consultas SET data_agendamento = ?, id_paciente = ?, id_medico = ? WHERE ROWID = ?;"
        cursor.execute(sql, [data["data_agendamento"], data["id_paciente"], data["id_medico"], id])
        conn.commit()
            
        
    
    def delete(self, id):
        sql = "DELETE FROM consultas WHERE ROWID = ?"
        cursor.execute(sql, [id])
        conn.commit()
        
    def get(self, id: int | None = None):
        sql =  """
           SELECT 
            consultas.ROWID AS id, 
            consultas.data_agendamento, 
            pacientes.nome, 
            medicos.nome,
            pacientes.cpf
            FROM
                consultas
            INNER JOIN 
                pacientes ON pacientes.ROWID = id_paciente
            INNER JOIN 
                medicos ON medicos.ROWID = id_medico
            
        """
        if id is not None:
            sql += "\nWHERE id = ?"
            cursor.execute(sql, [id])
            
            return cursor.fetchone()
        
        cursor.execute(sql)  
        return cursor.fetchall()

instance = Consulta()