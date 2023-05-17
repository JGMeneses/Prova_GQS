from ConexaoDB import *
def Q1(bd, cod):
        query = "SELECT MAX(media) FROM Media_aluno_turma INNER JOIN Turma ON Media_aluno_turma.id_turma = Turma.id WHERE Turma.codigo = ?"
        return ler_bd(bd, query, (cod,))
def Q2(bd, nome):
    query = "SELECT Turma.nome, Media_aluno_turma.media FROM Media_aluno_turma " \
            "INNER JOIN Turma ON Media_aluno_turma.id_turma = Turma.id " \
            "INNER JOIN Aluno ON Media_aluno_turma.id_aluno = Aluno.id " \
            "WHERE Aluno.nome = ?"
    return ler_bd(bd, query, (nome,))


def Q4(bd,nota):
    query = "SELECT DISTINCT Turma.nome FROM Turma " \
            "JOIN Media_aluno_turma ON Turma.id = Media_aluno_turma.id_turma " \
            "WHERE Media_aluno_turma.media >=?"
    return ler_bd(bd, query, (nota,))


