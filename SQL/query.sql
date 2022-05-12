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