INSERT INTO tipo_unidade (nome) VALUES ('Hospital');
INSERT INTO tipo_unidade (nome) VALUES ('Clínica');
INSERT INTO tipo_unidade (nome) VALUES ('Laboratório');
INSERT INTO tipo_unidade (nome) VALUES ('Home Care');

INSERT INTO sexo (nome) VALUES ('Masculino');
INSERT INTO sexo (nome) VALUES ('Feminino');
INSERT INTO sexo (nome) VALUES ('Outro');

INSERT INTO tipo_profissional (nome) VALUES ('Médico');
INSERT INTO tipo_profissional (nome) VALUES ('Enfermeiro');
INSERT INTO tipo_profissional (nome) VALUES ('Técnico');
INSERT INTO tipo_profissional (nome) VALUES ('Outro');

INSERT INTO especialidade (nome) VALUES ('Cardiologia');
INSERT INTO especialidade (nome) VALUES ('Dermatologia');
INSERT INTO especialidade (nome) VALUES ('Pneumologia');
INSERT INTO especialidade (nome) VALUES ('Pediatria');
INSERT INTO especialidade (nome) VALUES ('Neurologia');

INSERT INTO leito_status (nome) VALUES ('Livre');
INSERT INTO leito_status (nome) VALUES ('Ocupado');
INSERT INTO leito_status (nome) VALUES ('Manutenção');

INSERT INTO consulta_status (nome) VALUES ('Agendada');
INSERT INTO consulta_status (nome) VALUES ('Concluída');
INSERT INTO consulta_status (nome) VALUES ('Cancelada');

INSERT INTO perfil (nome) VALUES
('admin'),
('medico'),
('enfermeiro'),
('secretaria'),
('coordenador'),
('paciente');

INSERT INTO permissao (codigo, descricao) VALUES
('usuario.criar', 'Pode criar usuários'),
('usuario.editar', 'Pode editar usuários'),
('usuario.deletar', 'Pode deletar usuários'),
('usuario.visualizar', 'Pode visualizar usuários'),
('usuario.definir_permissoes', 'Pode definir permissões e perfis');

INSERT INTO permissao (codigo, descricao) VALUES
('paciente.criar', 'Pode cadastrar pacientes'),
('paciente.editar', 'Pode editar dados de pacientes'),
('paciente.deletar', 'Pode remover pacientes'),
('paciente.visualizar', 'Pode visualizar informações de pacientes');

INSERT INTO permissao (codigo, descricao) VALUES
('profissional.criar', 'Pode cadastrar profissionais'),
('profissional.editar', 'Pode editar profissionais'),
('profissional.deletar', 'Pode deletar profissionais'),
('profissional.visualizar', 'Pode visualizar profissionais');

INSERT INTO permissao (codigo, descricao) VALUES
('consulta.agendar', 'Pode agendar consultas'),
('consulta.editar', 'Pode editar consultas'),
('consulta.cancelar', 'Pode cancelar consultas'),
('consulta.realizar', 'Pode realizar consulta médica'),
('consulta.visualizar', 'Pode visualizar consultas');

INSERT INTO permissao (codigo, descricao) VALUES
('exame.solicitar', 'Pode solicitar exames'),
('exame.lancar_resultado', 'Pode lançar resultados de exames'),
('exame.visualizar', 'Pode visualizar exames');

INSERT INTO permissao (codigo, descricao) VALUES
('internacao.registrar', 'Pode registrar internações'),
('internacao.alterar', 'Pode alterar internações'),
('internacao.visualizar', 'Pode visualizar internações'),

('leito.alocar', 'Pode alocar leitos'),
('leito.liberar', 'Pode liberar leitos'),
('leito.visualizar', 'Pode visualizar leitos');

INSERT INTO permissao (codigo, descricao) VALUES
('suprimento.criar', 'Pode cadastrar suprimentos'),
('suprimento.editar', 'Pode editar suprimentos'),
('suprimento.deletar', 'Pode deletar suprimentos'),
('suprimento.visualizar', 'Pode visualizar suprimentos'),
('suprimento.baixar_estoque', 'Pode baixar quantidade do estoque'),
('suprimento.repor_estoque', 'Pode repor quantidade do estoque');

INSERT INTO permissao (codigo, descricao) VALUES
('movimentacao.criar', 'Pode registrar movimentações'),
('movimentacao.editar', 'Pode editar movimentações'),
('movimentacao.deletar', 'Pode deletar movimentações'),
('movimentacao.visualizar', 'Pode visualizar movimentações');


INSERT INTO perfil_permissao (perfil_id, permissao_id)
SELECT 1, id FROM permissao;

INSERT INTO perfil_permissao (perfil_id, permissao_id)
SELECT 2, id FROM permissao WHERE codigo IN (
    'paciente.visualizar',
    'profissional.visualizar',
    'consulta.visualizar',
    'consulta.realizar',
    'exame.solicitar',
    'exame.lancar_resultado',
    'exame.visualizar',
    'internacao.visualizar',
    'leito.visualizar',
    'suprimento.visualizar',
    'movimentacao.visualizar'
);
INSERT INTO perfil_permissao (perfil_id, permissao_id)
SELECT 3, id FROM permissao WHERE codigo IN (
    'paciente.visualizar',
    'paciente.editar',
    'consulta.visualizar',
    'exame.solicitar',
    'exame.visualizar',
    'internacao.visualizar',
    'leito.alocar',
    'leito.liberar',
    'leito.visualizar',
    'suprimento.visualizar',
    'suprimento.baixar_estoque',
    'movimentacao.criar',
    'movimentacao.visualizar'
);
INSERT INTO perfil_permissao (perfil_id, permissao_id)
SELECT 4, id FROM permissao WHERE codigo IN (
    'paciente.criar',
    'paciente.editar',
    'paciente.visualizar',
    'profissional.visualizar',
    'consulta.agendar',
    'consulta.editar',
    'consulta.cancelar',
    'consulta.visualizar',
    'suprimento.visualizar',
    'movimentacao.visualizar'
);
INSERT INTO perfil_permissao (perfil_id, permissao_id)
SELECT 5, id FROM permissao WHERE codigo IN (
    'paciente.criar','paciente.editar','paciente.visualizar',
    'profissional.criar','profissional.editar','profissional.visualizar',
    'consulta.agendar','consulta.editar','consulta.cancelar','consulta.realizar','consulta.visualizar',
    'exame.solicitar','exame.lancar_resultado','exame.visualizar',
    'internacao.visualizar',
    'leito.alocar','leito.liberar','leito.visualizar',
    'usuario.visualizar',
    'suprimento.visualizar',
    'movimentacao.visualizar'
);
INSERT INTO perfil_permissao (perfil_id, permissao_id)
SELECT 6, id FROM permissao WHERE codigo IN (
    'paciente.visualizar',
    'consulta.visualizar',
    'exame.visualizar'
);
