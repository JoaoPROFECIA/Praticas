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

