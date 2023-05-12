from MockDB import MockBD

import unittest
from MockDB import MockBD
from ConexaoDB import *
from queries_Professores import *

        
class TestProfessorDB(MockBD):
    def test_ler_todos_professores(self):
        # Teste 1: Todos os professores
        query = "SELECT * FROM Professor"
        retorno_esperado1 = [(1, 'Guilherme'), (2, 'Carla'), (3, 'Taniro'),(4, 'Alessandra')]

        self.assertEqual(ler_bd(self.mock_db_config.get('bd'), query), retorno_esperado1)

   

if __name__ == '__main__':
    unittest.main()