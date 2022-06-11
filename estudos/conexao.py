import mysql.connector

conexao = mysql.connector.connect(host='localhost',
                                  user='root',
                                  password='ColoqueSuaSenhaAQUI')

print("Conexão: ",conexao)
cursor = conexao.cursor()
sql = "CREATE DATABASE IF NOT EXISTS estudos"
cursor.execute(sql)
cursor.close()
conexao.close()
print("Conexão Fechada")