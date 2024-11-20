from model.Model import Model
from db import conn, cursor
from hashlib import sha256

class Medico(Model):
    def get(self):
        sql = "SELECT ROWID AS id, nome, idade, especialidade FROM medicos;"
        cursor.execute(sql)
        return cursor.fetchall()
    
    def get_by_id(self, id):
        sql = "SELECT ROWID AS id, nome, idade, especialidade FROM medicos WHERE id = ?;"
        cursor.execute(sql, [id])
        
        return cursor.fetchone()
    
    def register(self, email, senha, nome, data_nascimento, idade):
        sql = "INSERT INTO medicos (email, senha, nome, data_nascimento, idade) VALUES (?,?,?,?,?)"
        cursor.execute(sql, [email, self.__criptografia_senha(senha), nome, data_nascimento, idade])
        
        conn.commit()
        
    def authenticate(self, email: str, senha: str):
        sql = "SELECT ROWID as id FROM medicos WHERE email = ? AND senha = ? "
        cursor.execute(sql, [email, self.__criptografia_senha(senha)])
        
        data = cursor.fetchone()
        
        return None if data is None else data[0]
    
    def __criptografia_senha(self, senha: str):
        senha_segura = sha256(senha.encode()).hexdigest()
        return senha_segura
        

instance = Medico()