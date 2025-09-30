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
