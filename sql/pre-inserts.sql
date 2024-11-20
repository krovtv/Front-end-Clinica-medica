-- Pacientes Pré-Inseridos
INSERT INTO pacientes (nome, idade, cpf) VALUES 
('João Pereira', 30, '12345678901'),
('Maria Silva', 25, '23456789012'),
('Carlos Santos', 40, '34567890123'),
('Ana Oliveira', 35, '45678901234'),
('Pedro Costa', 50, '56789012345'),
('Júlia Almeida', 28, '67890123456'),
('Ricardo Lima', 45, '78901234567'),
('Beatriz Ferreira', 32, '89012345678'),
('Lucas Rocha', 29, '90123456789'),
('Fernanda Ribeiro', 38, '01234567890');

INSERT INTO especialidades (nome, descricao) VALUES
('Cardiologia', 'Especialidade médica que trata de doenças relacionadas ao coração e ao sistema circulatório.'),
('Dermatologia', 'Ramo da medicina que trata da pele, cabelos, unhas e mucosas.'),
('Neurologia', 'Área dedicada ao diagnóstico e tratamento de doenças do sistema nervoso central e periférico.'),
('Pediatria', 'Especialidade que cuida da saúde de bebês, crianças e adolescentes.'),
('Ortopedia', 'Ramo da medicina focado no tratamento de problemas nos ossos, músculos, articulações e ligamentos.'),
('Gastroenterologia', 'Especialidade que trata de doenças do sistema digestivo.'),
('Oftalmologia', 'Área da medicina que cuida dos olhos e da visão.'),
('Psiquiatria', 'Ramo da medicina que lida com a saúde mental e transtornos psiquiátricos.'),
('Ginecologia', 'Especialidade que trata da saúde do sistema reprodutor feminino.'),
('Endocrinologia', 'Ramo da medicina que estuda e trata os hormônios e as glândulas do corpo.');


INSERT INTO tipo_exame (nome, descricao) VALUES
('Hemograma', 'Exame para avaliar a saúde geral e detectar doenças como anemia e infecções'),
('Eletrocardiograma', 'Exame para verificar o funcionamento do coração através de sinais elétricos'),
('Raio-X', 'Exame de imagem para análise de ossos e tecidos'),
('Ultrassom', 'Exame de imagem para avaliar órgãos internos e gravidez'),
('Resonância Magnética', 'Exame para obter imagens detalhadas do corpo usando campos magnéticos e ondas de rádio'),
('Teste de Glicemia', 'Exame para medir os níveis de glicose no sangue'),
('Endoscopia', 'Exame para visualizar o interior do trato digestivo superior'),
('Exame de Urina', 'Análise laboratorial da urina para identificar infecções ou doenças renais'),
('Exame de Colesterol', 'Verificação dos níveis de colesterol e lipídios no sangue'),
('Mamografia', 'Exame de imagem para detectar anormalidades nas mamas');


