from model.Model import Model
from db import conn, cursor
from hashlib import sha256

class Funcionario(Model):
    def create(self, data):
        sql = 'INSERT INTO funcionarios(nome, idade, cargo, data_nascimento, email, senha) VALUES (?,?,?,?,?,?)'
        
        cursor.execute(sql, [data['nome'], data['idade'], data['cargo'], data['data_nascimento'], data['email'], self.__criptografia_senha(data['senha'])])
        conn.commit()
        
    
    def authorize(self, email, senha):
        sql = 'SELECT ROWID as id FROM funcionarios WHERE email = ? AND senha = ?'
        
        cursor.execute(sql, [email, self.__criptografia_senha(senha)])
        data = cursor.fetchone()
        return None if data is None else data[0]
    
    def __criptografia_senha(self, senha: str):
        senha_segura = sha256(senha.encode()).hexdigest()
        
        return senha_segura
        

instance = Funcionario()