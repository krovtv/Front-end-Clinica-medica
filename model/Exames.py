import random
import string
from model.Model import Model
from db import conn, cursor

class Exame(Model):
    def get(self, id:int = None):
        sql = """
            SELECT exames.ROWID AS id, protocolo, data_pedido, data_entrega, foi_entregue, pacientes.nome, tipo_exame.nome, pacientes.cpf, tipo_exame.ROWID
            FROM exames
            INNER JOIN 
                pacientes ON pacientes.ROWID = exames.id_paciente
            INNER JOIN 
                tipo_exame ON tipo_exame.ROWID = exames.tipo_exame
        """
        
        if id is  None:
            cursor.execute(sql)
            return cursor.fetchall()
        
        sql += "\nWHERE id = ?"
        cursor.execute(sql, [id])
        return cursor.fetchone()
    
    def get_by_cpf(self, cpf):
        sql = """
            SELECT ROWID AS id, protocolo, data_pedido, data_entrega, foi_entregue, pacientes.nome, tipo_exame.nome
            FROM exames
            INNER JOIN pacientes ON pacientes.ROWID = exames.id_paciente
            INNER JOIN tipo_exame ON tipo_exame.ROWID = exames.tipo_exame
            WHERE pacientes.cpf = ?
        """
        
        
        cursor.execute(sql, [cpf])
        return cursor.fetchall()
    
    def create(self, data):
        sql = 'INSERT INTO exames (protocolo, data_entrega, id_paciente, tipo_exame) VALUES (?,?,?,?)'
        
        data['protocolo'] = self.create_protocol()
        
        cursor.execute(sql, [data['protocolo'], data['data_entrega'], data['id_paciente'], data['tipo_exame']])
        conn.commit()
    
    
    def delete(self, id):
        sql = "DELETE FROM exames WHERE ROWID = ?"
        cursor.execute(sql, [id])
        conn.commit()
        
    
    def update(self, data, id):
        sql = """UPDATE exames 
            SET
                data_entrega = ?, 
                id_paciente = ?, 
                tipo_exame = ?
            WHERE ROWID = ?;
        """
        
        cursor.execute(sql, [data['data_entrega'], data['id_paciente'], data['tipo_exame'], id])
        conn.commit()
        
    
    def create_protocol(self,):
        while True:
            protocolo = ''.join(random.choices(string.ascii_letters + string.hexdigits, k=6))
            if not self.protocol_exists(protocolo):
                return protocolo
            
    
    def protocol_exists(self, protocolo: str):
        sql = "SELECT COUNT(protocolo) FROM exames WHERE protocolo = ?"
        
        cursor.execute(sql, [protocolo])
        return bool(cursor.fetchone()[0])
    
    def alter_recebimento_exame(self, id, foi_entregue: bool):
        sql = """UPDATE exames 
            SET
                foi_entregue = ?
            WHERE ROWID = ?;
        """
        
        cursor.execute(sql, [foi_entregue, id])
        conn.commit()
    
instance = Exame()