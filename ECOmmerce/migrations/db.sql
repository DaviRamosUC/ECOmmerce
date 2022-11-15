CREATE DATABASE ecommerce;


CREATE TABLE endereco (
  id BIGINT PRIMARY KEY AUTOINCREMENT,
  logradouro VARCHAR(120) NOT NULL,
  numero VARCHAR(10),
  complemento VARCHAR(50),
  bairro VARCHAR(80) NOT NULL,
  estado VARCHAR(20) NOT NULL,
  cep VARCHAR(9) NOT NULL,
);

CREATE TABLE usuario(
  id BIGINT PRIMARY KEY AUTOINCREMENT,
  nomeUsuario VARCHAR(60) NOT NULL,
  cpf VARCHAR(11) UNIQUE,
  cnpj VARCHAR(13) UNIQUE,
  celular VARCHAR(12) NOT NULL,
  email VARCHAR(20) UNIQUE NOT NULL,
  tipoUsuario char(2) NOT NULL,
  senha VARCHAR(20) NOT NULL,
  endereco_id BIGINT NOT NULL,

  FOREIGN KEY (endereco_id) REFERENCES endereco(id)
);

CREATE TABLE categoria(
  id BIGINT PRIMARY KEY AUTOINCREMENT,
  nomeCategoria VARCHAR(20) NOT NULL,
);


CREATE TABLE produto (
  id BIGINT PRIMARY KEY AUTOINCREMENT,
  nomeProduto VARCHAR(50) NOT NULL,
  preco double NOT NULL default 0,
  categoria_produto_id BIGINT NOT NULL,

);

CREATE TABLE categoria_produto(
  id BIGINT PRIMARY KEY AUTOINCREMENT,
  categoria_id BIGINT NOT NULL,
  produto_id BIGINT NOT NULL,

  FOREIGN KEY (categoria_id) REFERENCES categoria(id),
  FOREIGN KEY (produto_id) REFERENCES produto(id)
); 