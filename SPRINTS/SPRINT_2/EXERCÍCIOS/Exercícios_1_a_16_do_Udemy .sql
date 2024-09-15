-------Exercícios do Udemy Seção 3   ----------- banco de dados biblioteca
---banco de dados biblioteca
---tabela autor (codautor, nome, nascimento)
---editora (codeditora, nome, endereço)
--endereço (codendereco, pais, estado, cidade)
---livro (cod, titulo, autor, editora, valor, publicação, edição, idioma)

---Exercícios 01 
--Apresente a query para listar todos os livros publicados após 2014. Ordenar pela coluna cod, em ordem crescente, as linhas.  Atenção às colunas esperadas no resultado final: cod, titulo, autor, editora, valor, publicacao, edicao, idioma
SELECT  cod, titulo, autor, editora, valor, publicacao, edicao, idioma 
from livro WHERE publicacao > '2014-12-31' ORDER by cod
---Exercícios 02
--Apresente a query para listar os 10 livros mais caros. Ordenar as linhas pela coluna valor, em ordem decrescente.  Atenção às colunas esperadas no resultado final:  titulo, valor.
SELECT  titulo, valor from livro ORDER by valor desc limit 10
---Exercícios 03 
--Apresente a query para listar as 5 editoras com mais livros na biblioteca. O resultado deve conter apenas as colunas quantidade, nome, estado e cidade. Ordenar as linhas pela coluna que representa a quantidade de livros em ordem decrescente.
SELECT COUNT(li.cod) AS quantidade, 
editora.nome, endereco.estado, endereco.cidade
FROM livro li
JOIN editora ON li.editora = editora.codeditora
JOIN endereco ON editora.endereco = endereco.codendereco
GROUP BY editora.nome, endereco.estado, endereco.cidade
ORDER BY quantidade DESC LIMIT 5;
---Exercícios 04 
--Apresente a query para listar a quantidade de livros publicada por cada autor. Ordenar as linhas pela coluna nome (autor), em ordem crescente. Além desta, apresentar as colunas codautor, nascimento e quantidade (total de livros de sua autoria).
SELECT a.codautor, a.nome, a.nascimento,
    COUNT(l.cod) AS quantidade
FROM autor a
LEFT JOIN livro l ON a.codautor = l.autor
GROUP BY  a.codautor, a.nome, a.nascimento
ORDER BY a.nome ASC;
---Exercícios 05 
--Apresente a query para listar o nome dos autores que publicaram livros através de editoras NÃO situadas na região sul do Brasil. Ordene o resultado pela coluna nome, em ordem crescente. Não podem haver nomes repetidos em seu retorno. 
select distinct  atr.nome
from livro as book
	left join autor as atr on book.autor = atr.codAutor
	left join editora as edit on book.editora = edit.codEditora
	join endereco as adress on  
	edit.endereco = adress.codEndereco
where adress.estado not in ('SANTA CATARINA','RIO GRANDE DO SUL', 'PARANÁ')
order by atr.nome
---Exercícios 06
-- Apresente a query para listar o autor com maior número de livros publicados. O resultado deve conter apenas as colunas codautor, nome, quantidade_publicacoes.
SELECT a.codautor, a.nome, COUNT(l.cod) AS quantidade_publicacoes
FROM autor a
JOIN livro l ON a.codautor = l.autor
GROUP BY a.codautor, a.nome
ORDER BY quantidade_publicacoes DESC
---Exercícios 07 Apresente a query para listar o nome dos autores com nenhuma publicação. Apresentá-los em ordem crescente.
SELECT a.nome
FROM autor a
LEFT JOIN livro l ON a.codautor = l.autor
WHERE l.cod IS NULL
ORDER BY a.nome ASC;

------------------------Exercícios do Udemy Seção 4   -----------
--Exercícios 08- Apresente a query para listar o código e o nome do vendedor com maior número de vendas (contagem), e que estas vendas estejam com o status concluída.  As colunas presentes no resultado devem ser, portanto, cdvdd e nmvdd.
SELECT tbvendedor.cdvdd, tbvendedor.nmvdd
FROM tbvendedor
JOIN tbvendas on tbvendas.cdvdd = tbvendedor.cdvdd
WHERE tbvendas.status = 'Concluído'
GROUP BY tbvendedor.cdvdd, tbvendedor.nmvdd
 ORDER by COUNT(tbvendas.cdvdd) DESC
LIMIT 1;
---Exercícios 09 
--Apresente a query para listar o código e nome do produto mais vendido entre as datas de 2014-02-03 até 2018-02-02, e que estas vendas estejam com o status concluída. As colunas presentes no resultado devem ser cdpro e nmpro.
SELECT tbvendas.cdpro, tbvendas.nmpro
FROM tbvendas
WHERE tbvendas.status = 'Concluído' AND
	tbvendas.dtven	between '2014-02-03' and '2018-02-02'
GROUP BY tbvendas.cdpro, tbvendas.nmpro
ORDER BY count(tbvendas.qtd) DESC
LIMIT 1;
---Exercícios 10
--A comissão de um vendedor é definida a partir de um percentual sobre o total de vendas (quantidade * valor unitário) por ele realizado. O percentual de comissão de cada vendedor está armazenado na coluna perccomissao, tabela tbvendedor. Com base em tais informações, calcule a comissão de todos os vendedores, considerando todas as vendas armazenadas na base de dados com status concluído.   As colunas presentes no resultado devem ser vendedor, valor_total_vendas e comissao. O valor de comissão deve ser apresentado em ordem decrescente arredondado na segunda casa decimal.
SELECT 
    vd.nmvdd AS vendedor,
    SUM(v.qtd * v.vrunt) AS valor_total_vendas,
    ROUND(SUM(v.qtd * v.vrunt) * vd.perccomissao / 100, 2) AS comissao
FROM tbvendas v
JOIN tbvendedor vd ON v.cdvdd = vd.cdvdd
WHERE v.status = 'Concluído'
GROUP BY vd.nmvdd
ORDER BY comissao DESC;
---Exercícios 11
---Apresente a query para listar o código e nome cliente com maior gasto na loja. As colunas presentes no resultado devem ser cdcli, nmcli e gasto, esta última representando o somatório das vendas (concluídas) atribuídas ao cliente.
SELECT cdcli,nmcli,
    SUM(vrunt * qtd) AS gasto
FROM  tbvendas
WHERE lower(tbvendas.status) = lower('Concluído')
GROUP BY cdcli,nmcli
ORDER BY gasto DESC
LIMIT 1;

---Exercícios 12
---Apresente a query para listar código, nome e data de nascimento dos dependentes do vendedor com menor valor total bruto em vendas (não sendo zero). As colunas presentes no resultado devem ser cddep, nmdep, dtnasc e valor_total_vendas.
--Observação: Apenas vendas com status concluído.
SELECT d.cddep,d.nmdep,d.dtnasc, 
    SUM(v.vrunt * v.qtd) AS valor_total_vendas
FROM tbdependente d
JOIN tbvendedor vdd ON d.cdvdd = vdd.cdvdd
JOIN tbvendas v ON v.cdvdd = vdd.cdvdd
WHERE lower(v.status) = lower('concluído')
GROUP BY d.cddep, d.nmdep, d.dtnasc, vdd.cdvdd
HAVING SUM(v.vrunt * v.qtd) > 0
ORDER BY valor_total_vendas
LIMIT 1;

---Exercícios 13
--Apresente a query para listar os 10 produtos menos vendidos pelos canais de E-Commerce ou Matriz (Considerar apenas vendas concluídas).  As colunas presentes no resultado devem ser cdpro, nmcanalvendas, nmpro e quantidade_vendas.

SELECT v.cdpro, v.nmcanalvendas, v.nmpro, 
    SUM(v.qtd) AS quantidade_vendas
FROM  tbvendas v
WHERE lower(v.status) = lower('concluído') 
GROUP BY v.cdpro, v.nmcanalvendas, v.nmpro
ORDER BY quantidade_vendas ASC
LIMIT 10;

---Exercícios 14
--Apresente a query para listar o gasto médio por estado da federação. As colunas presentes no resultado devem ser estado e gastomedio. Considere apresentar a coluna gastomedio arredondada na segunda casa decimal e ordenado de forma decrescente.
--Observação: Apenas vendas com status concluído.
SELECT v.estado, 
    ROUND(AVG(v.qtd * v.vrunt), 2) AS gastomedio
FROM tbvendas v
WHERE LOWER(v.status) = LOWER('Concluído')
GROUP BY v.estado
ORDER BY gastomedio DESC;
---Exercícios 15
---Apresente a query para listar os códigos das vendas identificadas como deletadas. Apresente o resultado em ordem crescente.
SELECT cdven
FROM tbvendas
WHERE deletado = 1 
ORDER BY cdven ASC; 

---Exercícios 16
--Apresente a query para listar a quantidade média vendida de cada produto agrupado por estado da federação. As colunas presentes no resultado devem ser estado e nmprod e quantidade_media. Considere arredondar o valor da coluna quantidade_media na quarta casa decimal. Ordene os resultados pelo estado (1º) e nome do produto (2º).
--Obs: Somente vendas concluídas.

SELECT estado, nmpro, 
    ROUND(AVG(qtd), 4) AS quantidade_media
FROM tbvendas 
WHERE LOWER(status) = LOWER('Concluído') 
GROUP BY estado, nmpro
ORDER BY estado, nmpro asc
---========================================================================================
---Seção 6 do Data & Analytics- Exportação de Dados
--verificando a pasta uploads
----10 livros com maior valor
SELECT li.cod as codLivro, li.titulo as Titulo, au.codautor as codAutor,
au.nome as nomeAutor,li.valor as Valor,
ed.codeditora as CodEditora, ed.nome as nomeEditora
FROM livro li
JOIN autor au on li.autor = au.codautor
JOIN editora ed on li.editora = ed.codeditora
ORDER by valor DESC
LIMIT 10
---5 editores ccom maior quantidade de livros na biblioteca

SELECT COUNT(li.cod) AS quantidade, 
editora.nome, endereco.estado, endereco.cidade
FROM livro li
JOIN editora ON li.editora = editora.codeditora
JOIN endereco ON editora.endereco = endereco.codendereco
GROUP BY editora.nome, endereco.estado, endereco.cidade
ORDER BY quantidade DESC LIMIT 5;






