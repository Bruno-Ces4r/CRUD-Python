import mysql.connector

conexao = mysql.connector.connect(host='localhost',
                                  user='root',
                                  password='ColoqueSuaSenhaAQUI',
                                  database='estudos')

print("Conexão: ",conexao)
cursor = conexao.cursor()

sql = "SELECT * FROM tb_materias"
cursor.execute(sql)
registros = cursor.fetchall()
for index in registros:
    print(index)
deleta = "delete from tb_materias where id = %s"
escolha = int(input("Informe o id do item que deseja remover: "))
cursor.execute(deleta,[escolha])
conexao.commit()
print("Quantidade de registros deletados: ",cursor.rowcount)

cursor.close()
conexao.close()
print("Conexão is closed")