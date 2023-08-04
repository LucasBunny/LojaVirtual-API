CREATE DATABASE Loja_Virtual;

USE Loja_Virtual;

CREATE TABLE Produtos (
    id int NOT NULL AUTO_INCREMENT,
    codigoEAN int(13) NOT NULL,
    descricao varchar(50) NOT NULL,
    valor decimal(10, 2) NOT NULL,
    dataCadastro date NOT NULL,
    PRIMARY KEY (id)
);

INSERT INTO
    Produtos (codigoEAN, descricao, valor, dataCadastro)
VALUES
    (1684357912348, 'Boneca', 2.90, '2023-05-10');

INSERT INTO
    Produtos (codigoEAN, descricao, valor, dataCadastro)
VALUES
    (
        3584967135486,
        'Carrinho de Controle Remoto',
        35.00,
        '2023-05-10'
    );