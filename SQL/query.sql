##############################################
pip install pyodbc


import pyodbc

dados_conexao = (
    "Driver={SQL Server};"
    "Server=DESKTOP-F9TG7BE\SQLEXPRESS;"
    "Database=PythonSQL"
)


conexao = pyodbc.connect(dados_conexao)
print("Conexão Bom Sucedida")

cursor = conexao.cursor()

id = 4
cliente = "Lira"
produto = "Carro"
data_venda = "25/08/2021"
preco = 5000
quantidade = 1

comando = f"""INSERT INTO Vendas
VALUES
	({id}, '{cliente}', '{produto}', '{data_venda}', {preco}, {quantidade})"""

cursor.execute(comando)
cursor.commit()



############################################

SELECT DISTINCT coluna1,coluna2
FROM tabela;
/*
 mostra nomes sem duplicidade na tabela
*/

-- WHERE
SELECT coluna1,coluna2, coluna_n
FROM tabela
WHERE condição;

/*
OPERADOR    -    DESCRIÇÃO
=                IGUAL
>                MAIOR QUE
<                MENOR QUE
>=               MAIOR OU IGUAL
<=               MENOR OU IGUAL
<>               DIFERENTE DE
AND              OPERADOR LÓGICO E
OR               OPERADOR LÓGICO OU
*/

-- COUNT
SELECT COUNT(*) // COUNT(DISTINCT title)
FROM tabela

-- TOP
SELECT TOP 10 *
FROM tabela

-- ORDER BY
SELECT coluna1,coluna2
FROM tabela
ORDER BY coluna1 asc/desc

SELECT TOP 10 ProductID
FROM Production.Product
ORDER BY ListPrice desc

--Between
valor BETWEEN mínimo AND máximo

--IN
valor IN (valor1,valor2)
color IN ('blue','red')
valor IN (SELECT valor FROM nomeDaTabela)

-- LIKE
Vamos dizer que você quer encontrar uma pessoa 
no banco de dados mas não se lembra do nome inteiro...
SELECT * FROM person.person
WHERE FirstName like (começa em->) 'ovi%' 
                  (ou termina em->) '%to'

-- MIN MAX SUM AVG

-- GROUP BY
Divide o resultado da sua pesquisa em grupos
Para cada grupo que você aplicar uma função de agregação,
por exeplo:
    calcular a soma de itens
    contar o número de itens naquele grupo

SELECT coluna1,funcaoAgregacao(coluna2)
FROM nomeDaTabela
GROUP BY coluna1

-- HAVING
É basicamente muito usado em junção com o GROUP BY Para
filtrar resultados de um agrupamento.

De uma forma mais simples, é como um WHERE para dados 
agrupados.

SELECT coluna1,funcaoAgregacao(coluna2)
FROM nomeDaTabela
GROUP BY coluna1
HAVING condicao

A grande diferença entre HAVING e WHERE é que o GROUP BY
é aplicado depois que os dados já foram agrupados, enquanto 
o WHERE é aplicado antes dos dados serem agrupados.

Vamos dizer que queremos saber quais  nomes no sistema tem 
uma ocorrencia maior que 10 vezes:

SELECT FirstName, COUNT(FirstName) as "Quantidade"
FROM Person.Person
GROUP BY FirstName
HAVING COUNT(FirstName) > 10

Quais produtos não estão trazendo em média no mínimo 1M em total 
de vendas:

SELECT ProductID, AVG(linetotal)
FROM sales.SalesOrderDetail
GROUP BY ProductID
HAVING AVG(linetotal) < 1000000

-- AS
Serve para renomear, dar apelidos temporários para colunas, 
durante um select ou agregação

SELECT TOP 10 ListPrice as Preço / "Preço do produto"
FROM Production.Product

SELECT TOP 10 AVG(ListPrice) as Preço / "Preço Médio"
FROM Production.Product

Na pratica: 
    SELECT TOP 10 FirstName as Nome, LastName as Sobrenome
    FROM Person.Person

    SELECT top 10 productNumber as "Número do Produto"
    from Production.Product

    SELECT unitprice as "Preço unitário" FROM Sales.SalesOrderDetail



-- INNER JOIN
Existem 3 tipos gerais de JOINs:
    INNER JOIN, OUTER JOIN e SELF JOIN

Na pratica:
    SELECT pr.ListPrice, pr.Name, pc.Name
    FROM Production.Product Pr
    INNER JOIN Production.ProductSubcategory PC on 
    PC.ProductSubcategoryID = pr.ProductSubcategoryID