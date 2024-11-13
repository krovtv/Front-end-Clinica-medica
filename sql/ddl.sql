CREATE TABLE IF NOT EXISTS medicos(
	nome text NOT NULL,
	idade integer NOT NULL
);

CREATE TABLE IF NOT EXISTS pacientes(
	nome text NOT NULL,
	idade integer NOT NULL,
	cpf char(11) NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS consultas (
	id_medico integer NOT NULL,
	data_criacao datetime NOT NULL DEFAULT NOW,
	data_agendamento datetime NOT NULL,
	id_paciente integer NOT NULL,
	FOREIGN KEY (id_medico) REFERENCES medicos(rowid),
	FOREIGN KEY (id_paciente) REFERENCES paciente(rowid)
);

CREATE TABLE IF NOT EXISTS tipo_exame(
	nome text NOT NULL,
	descricao text NOT NULL
);

CREATE TABLE IF NOT EXISTS exames (
	protocolo char(6) NOT NULL unique,
	id_paciente integer NOT NULL,
	data_pedido datetime NOT NULL DEFAULT NOW,
	data_entrega datetime NOT NULL,
	tipo_exame integer NOT NULL,
	FOREIGN KEY (id_paciente) REFERENCES pacientes(rowid),
	FOREIGN KEY (tipo_exame) REFERENCES tipo_exame(rowid)
);

