import mysql.connector

conexao = mysql.connector.connect(host='localhost',
                                  user='root',
                                  password='ColoqueSuaSenhaAQUI',
                                  database='estudos')
print("Conexão: ",conexao)

cursor = conexao.cursor()

inserindo = '''INSERT INTO tb_materias(ra,nome,nota)
                VALUES(%s, %s, %s);'''
ra = input("Informe o RA do Aluno: ")
nome = input("Informe o nome da Matéria: ")
nota = float(input("Informe a nota do aluno: "))
cursor.execute(inserindo,[ra,nome,nota])
conexao.commit()
cursor.close()
conexao.close()
print("Conexão Fechada!")