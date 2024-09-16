-------------AQUI COMEÇA A CRIAÇÃO DAS TABELAS DIMENSIONAL ---------------------
------------------------------------fato_locacao------------------------------------------
CREATE TABLE fato_locacao (
    idLocacao INT PRIMARY KEY,
    dataLocacao DATE,
    horaLocacao TIME,
    dataEntrega DATE,
    horaEntrega TIME,
    qtdDiaria INT,
    vlrDiaria DECIMAL(10, 2),
    idVendedor INT,
    idCliente INT,
    idCarro INT,
    FOREIGN KEY (idVendedor) REFERENCES dim_vendedor(idVendedor),
    FOREIGN KEY (idCliente) REFERENCES dim_cliente(idCliente),
    FOREIGN KEY (idCarro) REFERENCES dim_carro(idCarro)   
);
---Migrando os  dados
INSERT OR REPLACE INTO fato_locacao (idLocacao, dataLocacao,  horaLocacao, dataEntrega,
horaEntrega,qtdDiaria, vlrDiaria, idVendedor,idCliente, idCarro )
SELECT idLocacao, dataLocacao,  horaLocacao,dataEntrega,horaEntrega,qtdDiaria,
vlrDiaria, idVendedor,idCliente, idCarro FROM tb_locacao;
----teste para ver se preenchimento
SELECT * FROM fato_locacao;
------------------------------------dim_vendedor-------------------------------------------
CREATE TABLE dim_vendedor (
    idVendedor INT PRIMARY KEY,
    nomeVendedor VARCHAR(100),
    sexoVendedor CHAR(1),    
    estadoVendedor VARCHAR(50)   
);
---Migrando os  dados
INSERT OR REPLACE INTO dim_vendedor (idVendedor,nomeVendedor, sexoVendedor, estadoVendedor)
SELECT idVendedor,nomeVendedor, sexoVendedor, estadoVendedor FROM tb_vendedor;
-------teste para ver se preenchimento
SELECT * from tb_vendedor;
SELECT * from dim_vendedor;
---------------------------------dim_cliente-----------------------------------------------
CREATE TABLE dim_cliente (
    idCliente INT PRIMARY KEY,
    nomeCliente VARCHAR(100),
    cidadeCliente VARCHAR(50),
    estadoCliente VARCHAR(50),
    paisCliente VARCHAR(50)
);
---Migrando os  dados
INSERT OR REPLACE INTO dim_cliente (idCliente, nomeCliente, 
cidadeCliente, estadoCliente, paisCliente)
SELECT idCliente, nomeCliente, cidadeCliente, 
estadoCliente, paisCliente FROM tb_cliente;
-------teste para ver se preenchimento
SELECT * from tb_cliente;
SELECT * from dim_cliente;

--------------------------------------dim_carro------------------------------------------
CREATE TABLE dim_carro (
    idCarro INT PRIMARY KEY,
    classiCarro VARCHAR(50),
    kmCarro INT,
    marcaCarro VARCHAR(50),
    modeloCarro VARCHAR(50),
    anoCarro YEAR,
    tipoCombustivel VARCHAR(50)
);
---Migrando os  dados
INSERT OR REPLACE INTO dim_carro (idCarro,classiCarro,
kmCarro,marcaCarro, modeloCarro, anoCarro, tipoCombustivel )
SELECT idCarro,classiCarro, kmCarro,marcaCarro,
modeloCarro, anoCarro, tipoCombustivel FROM tb_carro;
-------teste para ver se preenchimento

SELECT * from dim_carro;


SELECT dataLocacao,  horaLocacao, nomeVendedor, sexoVendedor,nomeCliente, 
cidadeCliente, modeloCarro, anoCarro, tipoCombustivel
from fato_locacao lo
join dim_vendedor ve on lo.idVendedor = ve.idVendedor
JOIN dim_cliente cl on lo.idCliente = cl.idCliente
JOIN dim_carro ca on lo.idCarro = ca.idCarro;

------------------------VIEWS DOS FATOS E DIMENSAO------------------------------------------------------------------------
CREATE VIEW v_fato_locacao AS
SELECT 
    f.idLocacao,
    f.dataLocacao,
    f.horaLocacao,
    f.dataEntrega,
    f.horaEntrega,
    f.qtdDiaria,
    f.vlrDiaria,
    v.nomeVendedor,
    c.nomeCliente,
    car.marcaCarro,
    car.modeloCarro,
    car.anoCarro,
    car.tipoCombustivel
FROM fato_locacao f
JOIN dim_vendedor v ON f.idVendedor = v.idVendedor
JOIN dim_cliente c ON f.idCliente = c.idCliente
JOIN dim_carro car ON f.idCarro = car.idCarro;

SELECT * FROM v_fato_locacao;

------------------------VIEWS v_dim_vendedor---------------------------------
CREATE VIEW v_dim_vendedor AS
SELECT 
    idVendedor,
    nomeVendedor,
    sexoVendedor,
    estadoVendedor
 FROM 
    dim_vendedor;
   
SELECT * FROM v_dim_vendedor;

------------------------VIEWS v_dim_cliente---------------------------------

CREATE VIEW v_dim_cliente AS
SELECT 
    idCliente,
    nomeCliente,
    cidadeCliente,
    estadoCliente,
    paisCliente
FROM 
    dim_cliente;
   
SELECT * FROM v_dim_cliente;

------------------------VIEWS v_dim_carro---------------------------------
   
   CREATE VIEW v_dim_carro AS
SELECT 
    idCarro,
    classiCarro,
    kmCarro,
    marcaCarro,
    modeloCarro,
    anoCarro,
    tipoCombustivel
FROM 
    dim_carro;

SELECT * FROM v_dim_carro;




