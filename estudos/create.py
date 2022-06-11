import mysql.connector

conexao = mysql.connector.connect(host='localhost',
                                  user='root',
                                  password='ColoqueSuaSenhaAQUI',
                                  database='estudos')

print("Conexão: ",conexao)
cursor = conexao.cursor()
curso = '''CREATE TABLE IF NOT EXISTS tb_materias(
        id int not null primary key auto_increment,
        ra varchar(255) not null,
        nome varchar(255) not null,
        nota decimal(9,2) not  null
            );'''

cursor.execute(curso)
cursor.close()
conexao.close()
print("Conexão Fechada!")