import mysql.connector

# import pyodbc
#
# dados_conexao = (
#     "Driver={SQL Server};"
#     "Server=DESKTOP-F9TG7BE\SQLEXPRESS;"
#     "Database=PythonSQL"
# )


# conexao = pyodbc.connect(dados_conexao)
# print("Conexão Bom Sucedida")
#
# cursor = conexao.cursor()


# CRUD

# Como conectar no Banco de Dados

# pip install mysql-connector-python (para instalar o conector do MySQL)


# Dados de conexão
dados_con = (host="localhost", database="nome do banco de dados", user="root", password="senha do banco de dados")

con = mysql.connector.connect(dados_con)  # Conectando no banco de dados

if con.is_connected():  # Verificando se a conexão foi bem sucedida
    db_info = con.get_server_info(),
    print("Conexão bem sucedida. Versão: ", db_info)

    cursor = con.cursor()
    cursor.execute("select database();")  # executar comando SQL
    linha = cursor.fetchone()  # pegar a primeira linha
    print("Conectado ao banco de dados: ", linha)

if con.is_connected():
    cursor.close()
    con.close()
    print("Conexão encerrada")

######################

# CREATE

# nome_produto = "toddy"
# valor = 3
# comando = f"""INSERT INTO Vendas2 (nome_produto, valor) VALUES ("{nome_produto}", {valor})"""
# cursor.execute(comando)
# cursor.commit()

# cursor.close()
# conexao.close()

######################

# READ

# comando = f"""SELECT * FROM Vendas2"""
# cursor.execute(comando)
# resultado = cursor.fetchall() # ler o banco de dados
# print(resultado)

######################

# UPDATE

# nome_produto = "toddy"
# valor = 6
# comando = f'UPDATE Vendas2 SET valor = {valor} WHERE nome_produto = "{nome_produto}"'
# cursor.execute(comando)
# cursor.commit()

######################

# DELETE

# nome_produto = "toddy"
# comando = f'DELETE FROM Vendas2 WHERE nome_produto = "{nome_produto}"'
# cursor.execute(comando)
# cursor.commit()
