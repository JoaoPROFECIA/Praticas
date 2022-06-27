import pyodbc

dados_conexao = (
    "Driver={SQL Server};"
    "Server=DESKTOP-F9TG7BE\SQLEXPRESS;"
    "Database=PythonSQL"
)


conexao = pyodbc.connect(dados_conexao)
print("Conexão Bom Sucedida")

cursor = conexao.cursor()


# CRUD



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