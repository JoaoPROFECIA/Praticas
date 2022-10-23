import mysql.connector
from mysql.connector import Error

try:
    con = mysql.connector.connect(host='localhost',
                                  database='nome do banco de dados',
                                  user='root',
                                  password='senha do banco de dados')
    consulta_sql = "SELECT * FROM Vendas2"
    cursor = con.cursor()
    cursor.execute(consulta_sql)
    linhas = cursor.fetchall()
    print("Total de registros: ", cursor.rowcount)
    print("\nMostrando os registros")
    for linha in linhas:
        print("Nome do produto: ", linha[0])
        print("Valor: ", linha[1], "\n")

except Error as e:
    print("Erro ao ler os dados do MySQL", e)

finally:
    if (con.is_connected()):
        cursor.close()
        con.close()
        print("Conexão ao MySQL encerrada")
