import mysql.connector

conexao = mysql.connector.connect(user='root',
                                  host='localhost',
                                  password='ColoqueSuaSenhaAQUI',
                                  database='estudos')

print("Conexão:", conexao)
cursor = conexao.cursor()

sql = "select * from tb_materias"

cursor.execute(sql)
tupla_registros = cursor.fetchall() #Joga em uma tupla

print("Registros na tabela: ",cursor.rowcount) # Quantidade de registros na tabela
print("-Lista de Tuplas:-")
for i in tupla_registros:
    print(i)

cursor.close()
conexao.close()
print("\n Conexão Fechada.")