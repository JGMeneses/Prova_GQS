from ConexaoDB import *

def ler_todos_aluno(bd, alunos):
    query = "SELECT * FROM Aluno"   
    return ler_bd(bd, query, (alunos,))

def select_aluno_por_id(bd, alunos):
    query = "SELECT * FROM Aluno WHERE id = ?"
    return ler_bd(bd, query, (alunos,))

def ler_aluno_por_nome(bd, alunos):
    query = "SELECT * FROM Aluno WHERE nome = ?"
    return ler_bd(bd, query, (alunos,))

def ler_aluno_por_id_turma(bd, alunos):
    query = "SELECT * FROM Aluno WHERE id_turma = ?"
    return ler_bd(bd, query, (alunos,))
