from MockDB import MockBD

import unittest
from MockDB import MockBD
from ConexaoDB import *
from query_prova import *


class TestProvaQuest(MockBD):
    
    def test_Q1(self):
        cod = 'TAD0203'
        retorno_esperado = [(9.3,)]

        resultado = Q1(self.mock_db_config.get('bd'), cod)
        self.assertEqual(resultado, retorno_esperado)

    def test_Q1_nota0(self):
        cod = 'TEST001'
        retorno_esperado = [(0.0,)]

        resultado = Q1(self.mock_db_config.get('bd'), cod)
        self.assertEqual(resultado, retorno_esperado)


    def test_Q2(self):
        retorno_esperado = [('2021.1', 8.0)]
        nome = 'Carla'
        resultado = Q2(self.mock_db_config.get('bd'), nome)
        self.assertEqual(resultado, retorno_esperado)
    
   

    def test_Q4(self):
        nota = 9.0
        retorno_esperado = [('2021.1',)]
        resultado = Q4(self.mock_db_config.get('bd'),nota)
        self.assertEqual(resultado, retorno_esperado)

    def test_Q4Nulo(self):
        nota = 10.0
        retorno_esperado = []
        resultado = Q4(self.mock_db_config.get('bd'),nota)
        self.assertEqual(resultado, retorno_esperado)

    



# Executar os testes
if __name__ == '__main__':
    unittest.main()
