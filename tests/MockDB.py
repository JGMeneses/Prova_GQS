from unittest import TestCase

import sys
sys.path.insert(0, '..')
from ConexaoDB import *

BD = "TestDB.db"

class MockBD(TestCase):
    @classmethod
    def setUpClass(cls):
        con = conectar(BD)
        cursor = con.cursor()

        # Medico: id(PK), nome, crm, especialidade
        # Paciente: id (PK), nome
        # Prontuario: id (PK), id_medico (FK), id_paciente(FK)
        # Exames: id (PK), nome, id_prontuario (FK), resultado
        query_create_Professor = """CREATE TABLE Professor (
                                    id INTEGER PRIMARY KEY,
                                    nome TEXT
                                )"""
        query_create_Aluno = """CREATE TABLE Aluno (
                                    id INTEGER PRIMARY KEY,
                                    nome TEXT
                                )"""
        query_create_Turma = """CREATE TABLE Turma (
                                    id INTEGER PRIMARY KEY,
                                    nome TEXT,
                                    codigo TEXT
                                )"""
        query_create_Media_aluno_turma = """CREATE TABLE Media_aluno_turma (
                                    id INTEGER PRIMARY KEY,
                                    id_turma INTEGER,
                                    id_aluno INTEGER,
                                    nota1 REAL,
                                    nota2 REAL,
                                    nota3 REAL,
                                    media REAL,
                                    FOREIGN KEY (id_turma) REFERENCES Turma (id),
                                    FOREIGN KEY (id_aluno) REFERENCES Aluno (id)
                                )"""
        try:
            cursor.execute(query_create_Professor)
            cursor.execute(query_create_Turma)
            cursor.execute(query_create_Aluno)
            cursor.execute(query_create_Media_aluno_turma)
            con.commit()
        except sqlite3.Error as error:
            print("Erro na criação das tabelas:", error)
        else:
            print("Criação das tabelas: OK")

        query_insert_Professor = """INSERT INTO Professor (id, nome) VALUES
                                    (1, 'Guilherme'),
                                    (2, 'Carla'),
                                    (3, 'Taniro'),
                                    (4, 'Alessandra')"""
        query_insert_Aluno = """INSERT INTO Aluno (id, nome) VALUES
                                    (1, 'João'),
                                    (2, 'Giovanna'),
                                    (3, 'David'),
                                    (4, 'Nahmias'),
                                    (5, 'Carla'),
                                    (6, 'Davi')"""
        query_insert_Turma = """INSERT INTO Turma (id, nome, codigo) VALUES
                                    (1, '2021.1', 'TAD0203'),
                                    (2, '2021.2', 'TEST001'),
                                    (3, '2022.1', 'TTEST002'),
                                    (4, '2022.2', 'TEST003')"""
        query_insert_Media_aluno_turma = """INSERT INTO Media_aluno_turma (id,id_turma, id_aluno, nota1, nota2, nota3, media) VALUES
                                    (1, 1, 3, 7.5, 8.0, 6.5, 7.3),
                                    (2, 1, 3, 6.0, 7.0, 8.0, 7.0),
                                    (3, 1, 3, 9.0, 9.5, 8.5, 9.0),
                                    (4, 1, 4, 9.5, 9.0, 9.5, 9.3),
                                    (5, 1, 5, 8.0, 7.5, 8.5, 8.0),
                                    (6, 5, 6, 9.5, 9.0, 9.5, 9.3),
                                    (7, 5, 6, 9.0, 9.5, 8.5, 9.0),
                                    (8, 6, 6, 9.5, 9.0, 9.5, 9.3),
                                    (9, 1, 1, 9.5, 9.0, 9.5, 9.3),
                                    (10, 6, 2, 9.5, 9.0, 9.5, 9.3)"""
        try:
            cursor.execute(query_insert_Professor)
            cursor.execute(query_insert_Aluno)
            cursor.execute(query_insert_Turma)
            cursor.execute(query_insert_Media_aluno_turma)
            con.commit()
        except sqlite3.Error as error:
            print("Erro na inserção de dados:", error)
        else:
            print("Inserção dos dados: OK")

        cursor.close()

        desconectar(con)

        testconfig ={
            'bd': BD
        }
        cls.mock_db_config = testconfig

    @classmethod
    def tearDownClass(cls):
        print("TearDown")
        con = conectar(BD)
        cursor = con.cursor()

        try:
            cursor.execute("DROP TABLE Professor")
            cursor.execute("DROP TABLE Aluno")
            cursor.execute("DROP TABLE Turma")
            cursor.execute("DROP TABLE Media_aluno_turma")
            con.commit()
            cursor.close()
            print("Removeu os dados das tabelas.")
        except sqlite3.Error as error:
            print("Banco de dados não existe. Erro na remoção do BD.", error)
        finally:
            desconectar(con)
