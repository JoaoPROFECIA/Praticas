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