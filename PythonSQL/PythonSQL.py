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