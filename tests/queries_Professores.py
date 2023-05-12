from ConexaoDB import *

def ler_todos_professore(bd, professor):
    query = "SELECT * FROM Professor"    
    return ler_bd(bd, query, (professor,))

def ler_professor_por_nome(bd, professor):
    query = "SELECT * FROM Professor WHERE nome = ?"
    return ler_bd(bd, query, (professor,))

def ler_professor_por_id_turma(bd, professor):
    query = "SELECT * FROM Professor WHERE id_turma = ?"
    return ler_bd(bd, query, (professor,))
