# Projeto RaD - Clínica Uniruymed+

Desenvolvido para a matéria **Desenvolvimento de Aplicações Rápidas em Python com a metodologia RaD**, este projeto simula as operações rotineiras de um sistema médico em um consultório. Ele permite o gerenciamento eficiente de pacientes, consultas, exames e profissionais da clínica.

------

## 🛠 Tecnologias Utilizadas

- **Flask** – Framework para desenvolvimento web em Python.
- **Bootstrap 4.6** – Framework para estilização responsiva.
- **SQLite3** – Banco de dados leve e eficiente.
- **jQuery** – Biblioteca JavaScript para manipulação dinâmica.

------

## 📋 Funcionalidades

O sistema foi projetado para atender às principais necessidades de uma clínica médica:

1. Pacientes:
   - Cadastro de pacientes.
2. Consultas:
   - Registro, consulta, alteração e exclusão de consultas.
3. Exames:
   - Registro, consulta, alteração e exclusão de exames.
   - Controle de entrega e cancelamento de exames.
4. Profissionais:
   - Criação de contas para médicos e funcionários.

------

## 🚀 Acesse o Projeto em Produção

O sistema já está disponível online. Utilize os links abaixo para acessar:

- [Login como Funcionário](https://front-end-clinica-medica.onrender.com/funcionario/login)
- [Login como Médico](https://front-end-clinica-medica.onrender.com/medico/login)

------

## 🖥 Como Rodar o Projeto Localmente

Siga os passos abaixo para configurar o projeto no seu ambiente:

1. **Ative o Ambiente Virtual do Python:**
   No Windows:

   ```powershell
   ./venv/Scripts/activate
   ```

   No Linux:

   ```powershell
   source ./venv/Scripts/activate
   ```

2. **Instale as Dependências:**

   ```powershell
   pip install -r requirements.txt
   ```

3. **Execute os Scripts para Configurar o Banco de Dados:**

   ```powershell
   python exec_scripts_db.py
   ```

4. **Inicie o Servidor:**
   No Windows:

   ```powershell
   python main.py
   ```

   No Linux:

   ```powershell
   python3 main.py
   ```

------

## 👥 Autores

- **Kaique Dias Pereira**
- **Jefferson Santos da Silva**
- **Kauã Victor Bomfim Guimarães de Almeida Oliveira**
