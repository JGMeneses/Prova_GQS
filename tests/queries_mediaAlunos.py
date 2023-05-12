from ConexaoDB import *
##Selecionar todas as médias:
def ler_Media_aluno_turma(bd, alunos):
    query = "SELECT * FROM Media_aluno_turma"  
    return ler_bd(bd, query, (alunos,))

##Selecionar todas as médias dos alunos por id
def select_Media_aluno_turma(bd, alunos):
    query = "SELECT * FROM Media_aluno_turma WHERE id_turma = ?"
    return ler_bd(bd, query, (alunos,))

##Selecionar médias dos alunos de uma turma específica:
def lery_select_medias_alunos_por_turma(bd, alunos):
    query = f"SELECT * FROM Media_aluno_turma WHERE id_turma =  ?"
    return ler_bd(bd, query, (alunos,))

##Selecionar alunos, turmas e suas respectivas médias:
def ler__select_alunos_turmas_medias(bd, alunos):
    query = "SELECT Aluno.*, Turma.*, Media_aluno_turma.* FROM Aluno JOIN Turma ON Aluno.id_turma = Turma.id JOIN Media_aluno_turma ON Aluno.id = Media_aluno_turma.id_aluno AND Turma.id = Media_aluno_turma.id_turma"
    return ler_bd(bd, query, (alunos,))

##Selecionar alunos e suas respectivas turmas:
def ler__select_alunos_turmas_medias(bd, alunos):
    query = "SELECT Aluno.*, Turma.*, Media_aluno_turma.* FROM Aluno JOIN Turma ON Aluno.id_turma = Turma.id JOIN Media_aluno_turma ON Aluno.id = Media_aluno_turma.id_aluno AND Turma.id = Media_aluno_turma.id_turma"
    return ler_bd(bd, query, (alunos,))

##Selecionar todas as médias dos alunos nas turmas:
def ler___select_medias_alunos_turmas(bd, alunos):
    query = "SELECT * FROM Media_aluno_turma"
    return ler_bd(bd, query, (alunos,))

###### POR MEDIA:

##Alunos de uma turma específica com notas acima de 7:
def ler_select_alunos_acima_de_7_por_turma(bd, alunos):
    query = "SELECT Aluno.* FROM Aluno JOIN Media_aluno_turma ON Aluno.id = Media_aluno_turma.id_aluno WHERE Media_aluno_turma.id_turma = ? AND Media_aluno_turma.media > 7"
    return ler_bd(bd, query, (alunos,))

##Alunos de todas as turmas com notas acima de 7:
def ler_select_alunos_acima_de_7 (bd, alunos):
    query = "SELECT Aluno.* FROM Aluno JOIN Media_aluno_turma ON Aluno.id = Media_aluno_turma.id_aluno WHERE Media_aluno_turma.media > 7"
    return ler_bd(bd, query, (alunos,))


##Alunos de uma turma específica com notas abaixo de 7:
def ler__select_alunos_abaixo_de_7_por_turma(bd, alunos):
    query  = "SELECT Aluno.* FROM Aluno JOIN Media_aluno_turma ON Aluno.id = Media_aluno_turma.id_aluno WHERE Media_aluno_turma.id_turma =  ? AND Media_aluno_turma.media < 7"
    return ler_bd(bd, query, (alunos,))

##Selecionar todas as médias dos alunos nas turmas:
def ler___select_medias_alunos_turmas(bd, alunos):
    query = "SELECT * FROM Media_aluno_turma"
    return ler_bd(bd, query, (alunos,))



