CREATE TABLE tipo_unidade (
    id SERIAL PRIMARY KEY,
    nome TEXT NOT NULL UNIQUE
);

CREATE TABLE unidade_saude (
    id SERIAL PRIMARY KEY,
    nome TEXT NOT NULL,
    tipo_unidade INTEGER NOT NULL REFERENCES tipo_unidade(id),
    endereco TEXT,
    email TEXT,
    telefone TEXT
);

CREATE TABLE sexo (
    id SERIAL PRIMARY KEY,
    nome TEXT NOT NULL UNIQUE
);

CREATE TABLE paciente (
    id SERIAL PRIMARY KEY,
    nome TEXT NOT NULL,
    cpf TEXT UNIQUE NOT NULL,
    data_nascimento DATE NOT NULL,
    sexo INTEGER NOT NULL REFERENCES sexo(id),
    endereco TEXT NOT NULL,
    telefone TEXT NOT NULL,
    email TEXT,
    id_unidade INTEGER NOT NULL REFERENCES unidade_saude(id)
);

CREATE TABLE tipo_profissional (
    id SERIAL PRIMARY KEY,
    nome TEXT NOT NULL UNIQUE
);

CREATE TABLE especialidade (
    id SERIAL PRIMARY KEY,
    nome TEXT NOT NULL UNIQUE
);

CREATE TABLE profissional (
    id SERIAL PRIMARY KEY,
    nome TEXT NOT NULL,
    tipo_profissional INTEGER NOT NULL REFERENCES tipo_profissional(id),
    especialidade INTEGER NOT NULL REFERENCES especialidade(id),
    registro TEXT NOT NULL,
    telefone TEXT NOT NULL,
    email TEXT NOT NULL,
    id_unidade INTEGER NOT NULL REFERENCES unidade_saude(id)
);

CREATE TABLE leito_status (
    id SERIAL PRIMARY KEY,
    nome TEXT NOT NULL UNIQUE
);

CREATE TABLE leito (
    id SERIAL PRIMARY KEY,
    numero TEXT NOT NULL UNIQUE,
    tipo TEXT,
    status INTEGER NOT NULL REFERENCES leito_status(id),
    id_unidade INTEGER NOT NULL REFERENCES unidade_saude(id)
);


CREATE TABLE suprimento (
    id SERIAL PRIMARY KEY,
    nome TEXT NOT NULL UNIQUE,
    tipo TEXT NOT NULL,
    quantidade_atual INTEGER NOT NULL,
    quantidade_minima INTEGER NOT NULL,
    id_unidade INTEGER NOT NULL REFERENCES unidade_saude(id)
);


CREATE TABLE movimentacao (
    id SERIAL PRIMARY KEY,
    tipo_movimentacao TEXT NOT NULL,
    quantidade INTEGER NOT NULL,
    data_hora TIMESTAMP NOT NULL,
    id_suprimento INTEGER NOT NULL REFERENCES suprimento(id),
    id_profissional INTEGER NOT NULL REFERENCES profissional(id)
);

CREATE TABLE consulta_status (
    id SERIAL PRIMARY KEY,
    nome TEXT NOT NULL UNIQUE
);

CREATE TABLE consulta (
    id SERIAL PRIMARY KEY,
    data_hora TIMESTAMP NOT NULL,
    status INTEGER NOT NULL REFERENCES consulta_status(id),
    id_paciente INTEGER NOT NULL REFERENCES paciente(id),
    id_profissional INTEGER NOT NULL REFERENCES profissional(id)
);

CREATE TABLE exame (
    id SERIAL PRIMARY KEY,
    tipo_exame TEXT NOT NULL,
    data_agendamento DATE NOT NULL,
    data_hora_realizacao TIMESTAMP NOT NULL,
    resultado TEXT NOT NULL,
    descricao TEXT,
    id_paciente INTEGER NOT NULL REFERENCES paciente(id),
    id_profissional INTEGER NOT NULL REFERENCES profissional(id)
);

CREATE TABLE internacao (
    id SERIAL PRIMARY KEY,
    descricao TEXT,
    data_hora_entrada TIMESTAMP NOT NULL,
    data_hora_saida TIMESTAMP,
    id_paciente INTEGER NOT NULL REFERENCES paciente(id),
    id_profissional INTEGER NOT NULL REFERENCES profissional(id),
    id_leito INTEGER NOT NULL REFERENCES leito(id)
);


CREATE TABLE administrador (
    id SERIAL PRIMARY KEY,
    nome TEXT NOT NULL UNIQUE,
    email TEXT NOT NULL,
    telefone TEXT NOT NULL,
    cargo TEXT NOT NULL
);

