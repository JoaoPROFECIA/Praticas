SELECT
-- SQL Server, PostgreSQL, MySQL, SQLite and Oracle

SELECT colunm1,colunm2
FROM table

SELECT * FROM table

/*
DESAFIO 1
A equipe de marketing precisa fazer uma pesquisa sobre nomes mais comuns de seus clientes
e precisa do nome e sobrenome de todos os clientes cadastrados no sistema.

first name, last name
*/

SELECT firstname, lastname FROM Person.Person;

/*
DESAFIO 2
Quantos sobrenomes únicos temos na tabela Person.Person?
*/
SELECT DISTINCT LastName 
FROM Person.Person;

SELECT DISTINCT coluna1, coluna2 
FROM tabela;

SELECT DISTINCT FirstName 
FROM Person.Person;


-- WHERE
SELECT coluna1,coluna2,coluna_n
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

SELECT * FROM Production.Product
where ListPrice > 1500 and ListPrice < 5000
where Color = 'blue' or Color = 'black'
where color <> 'red'

-- DESAFIO 3
/*
A equipe de podução de produtos precisa do nome de todas as peças que pesam mais de 500kg 
e não mais que 700kg para inspeção
*/
--weight > 500 and weight < 700

SELECT * FROM Production.Product
WHERE weight > 500 and weight <= 700

-- DESAFIO 4
/*
Foi solicitado pela equipe de marketing uma relação de todos os empregados (employees) que são casados
(single / married) e que são assalariados (salaried).
*/

SELECT * FROM HumanResources.Employee
WHERE MaritalStatus = 'M' and salariedflag = 1;

-- DESAFIO 5
/*
Um usuário chamado Peter Krebs está devendo um pagamento. Consiga o e-mail dele para que possamos enviar 
uma cobrança.
Tabelas: Person.Person e Person.EmailAddress
*/

SELECT * FROM Person.Person
WHERE FirstName = 'Peter' and LastName = 'Krebs';

SELECT * 
FROM Person.EmailAddress
WHERE BusinessEntityID = 26;

-- peter0@adventure-works.com

-- COUNT
SELECT COUNT(*) FROM tabela;
SELECT COUNT(DISTINCT coluna) FROM tabela;

SELECT count(*)
FROM Person.Person

SELECT count(distinct Title)
FROM Person.Person


/*
DESAFIO 6
Quantos produtos temos cadastrados em nossa tabela de produtos?
(Production.Product)
*/
SELECT COUNT(*)
FROM Production.Product

/*
DESAFIO 7
Quantos tamanhos de produtos temos cadastrados em nossa tabela?
(Production.produtc)
*/
SELECT COUNT(SIZE)
FROM Production.Product

/*
Quantos tamanhos diferentes de produtos temos cadastrados em nossa tabela?
(Production.product)
*/
SELECT COUNT(distinct SIZE)
FROM Production.Product


-- TOP
SELECT TOP 10 * FROM TABELA;

SELECT TOP 10 * FROM Production.Product
where color = 'blue';

-- ORDER BY
SELECT * FROM TABELA 
ORDER BY coluna ASC, coluna_n DESC;

SELECT *
FROM Person.Person
ORDER BY FirstName ASC, LastName desc

SELECT FirstName, LastName
FROM Person.Person
ORDER BY FirstName ASC, LastName desc

/*
DESAFIO 8
Obter o ProductID dos 10 produtos mais caros cadastrados na tabela, listando do mais caro para o mais barato.
*/

SELECT TOP 10 ProductID
FROM Production.Product
ORDER BY ListPrice desc

/*
DESAFIO 9
Obter o nome e número dos produtos que tem o ProductID entre 1 e 4
*/

SELECT Name, ProductNumber
FROM Production.Product
WHERE ProductID BETWEEN 1 and 4

SELECT TOP 4 Name, ProductNumber
FROM Production.Product
ORDER BY ProductID asc



-- BETWEEN
É usado para selecionar os valores entre um intervalo de valores mínimo e máximo.

Ex: 
WHERE ProductID BETWEEN 1 and 4

SELECT * FROM Production.Product
WHERE ListPrice BETWEEN 1000 and 1500

SELECT * FROM Production.Product
WHERE ListPrice not BETWEEN 1000 and 1500

SELECT * FROM HumanResources.Employee
WHERE HireDate between '2009-01-01' and '2010-01-01'
ORDER BY HireDate

-- IN
É usado para selecionar os valores que estão dentro de uma lista de valores.

Ex: 
WHERE ProductID IN (1,2,3,4)
OU
WHERE ProductID IN (SELECT ProductID FROM Production.Product WHERE Color = 'blue')

SELECT *
FROM Person.Person
WHERE BusinessEntityID IN (2,7,13)

