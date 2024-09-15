ALTER TABLE tb_locacao RENAME TO locacao
SELECT * FROM locacao

CREATE TABLE tb_locacao (
    idLocacao INT PRIMARY KEY,
    dataLocacao DATETIME,
    horaLocacao TIME,
    dataEntrega  DATE,
    horaEntrega TIME,
    qtdDiaria INT,
    vlrDiaria DECIMAL(10, 2),
    idVendedor INT,
    idCliente INT,
    idCarro INT,
    idCombustivel INT,
    FOREIGN KEY (idVendedor) REFERENCES tb_vendedor(idVendedor),
    FOREIGN KEY (idCliente) REFERENCES tb_cliente(idCliente),
    FOREIGN KEY (idCarro) REFERENCES tb_carro(idCarro),
    FOREIGN KEY (idCombustivel) REFERENCES tb_combustivel(idCombustivel)
);
---Migrando os  dados
INSERT OR REPLACE INTO tb_locacao (idLocacao, dataLocacao,  horaLocacao,dataEntrega,
horaEntrega,qtdDiaria, vlrDiaria, idVendedor,idCliente, idCarro, idCombustivel )
SELECT idLocacao, dataLocacao,  horaLocacao,dataEntrega,horaEntrega,qtdDiaria,
vlrDiaria, idVendedor,idCliente, idCarro, idCombustivel FROM locacao;

CREATE TABLE tb_vendedor (
    idVendedor INT PRIMARY KEY ,
    nomeVendedor VARCHAR(100),
    sexoVendedor CHAR(1),
    estadoVendedor VARCHAR(50)
);
---Migrando os  dados
INSERT OR REPLACE INTO tb_vendedor (idVendedor,nomeVendedor, sexoVendedor, estadoVendedor)
SELECT idVendedor,nomeVendedor, sexoVendedor, estadoVendedor FROM locacao;

CREATE TABLE tb_cliente (
    idCliente INT PRIMARY KEY ,
    nomeCliente VARCHAR(100),
    cidadeCliente VARCHAR(50),
    estadoCliente VARCHAR(50),
    paisCliente VARCHAR(50)
);
---Migrando os  dados
INSERT OR REPLACE INTO tb_cliente (idCliente, nomeCliente, 
cidadeCliente, estadoCliente, paisCliente)
SELECT idCliente, nomeCliente, cidadeCliente, 
estadoCliente, paisCliente FROM locacao;

CREATE TABLE tb_carro (
    idCarro INT PRIMARY KEY ,
    classiCarro VARCHAR(50),
    kmCarro INT,
    marcaCarro VARCHAR(50),
    modeloCarro VARCHAR(50),
    anoCarro INT,
    tipoCombustivel INT
);
---Migrando os  dados
INSERT OR REPLACE INTO tb_carro (idCarro,classiCarro,
kmCarro,marcaCarro, modeloCarro, anoCarro, tipoCombustivel )
SELECT idCarro,classiCarro, kmCarro,marcaCarro,
modeloCarro, anoCarro, tipoCombustivel FROM locacao;


CREATE TABLE tb_combustivel (
    id_Combustivel INT PRIMARY KEY ,
    tipo_Combustivel VARCHAR(50)
);
---Migrando os  dados
USE concessionaria;
INSERT OR REPLACE INTO tb_combustivel (id_Combustivel, tipo_Combustivel )
SELECT idCombustivel, tipoCombustivel FROM locacao;



------REALIAZDO ALGUNS TESTES COM AS NOVAS TABELAS

SELECT * FROM tb_locacao;
SELECT * FROM tb_cliente;
SELECT * FROM tb_vendedor;

SELECT l.dataLocacao, v.nomeVendedor AS vendedor, c.nomeCliente AS cliente,
car.modeloCarro AS modelo_car, com.tipo_Combustivel AS combustivel
FROM  tb_locacao L
JOIN tb_vendedor v ON v.idVendedor = l.idVendedor 
JOIN tb_cliente c ON c.idCliente = l.idCliente 
JOIN tb_carro car ON car.idCarro  = l.idCarro
JOIN tb_combustivel com ON com.id_Combustivel  = l.idCombustivel ;





