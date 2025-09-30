from db import connect 
def criar_aluno(nome, idade):
    conexao, cursor = connect()
    if conexao:
        try:
            cursor.execute(
                "INSERT INTO alunos (nome, idade) VALUES (%s, %s)", 
                (nome, idade)
            )
            conexao.commit()
        except Exception as erro:
            print(f'Erro ao inserir: {erro}')
        finally:
            cursor.close()
            conexao.close()
def listar_alunos():
    conexao, cursor = connect()
    if conexao:
        try:
            cursor.execute(
                "SELECT * FROM alunos ORDER BY id" # ordena por id
                )
            return cursor.fetchall()  # fetchall traz todos os registros
        except Exception as erro:
            print(f'Erro ao listar: {erro}')
            return [] # retorna lista vazia em caso de erro
        finally: 
            cursor.close()
            conexao.close()

def atualizar_alunos(id_aluno, nova_idade):
    conexao, cursor = connect()
    if conexao:
        try:
            cursor.execute( 
                "UPDATE alunos SET idade = %s WHERE id = %s", 
                (nova_idade, id_aluno)
            )
        except Exception as erro:
            print(f'Erro ao atualizar um aluno: {erro}')
        finally:
                
            cursor.close()
            conexao.close()



