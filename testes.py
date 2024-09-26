import unittest
from analise import analisar_texto

class TestAnalise(unittest.TestCase):
    def test_analisar_texto(self):
        texto = "Este é um exemplo de texto com erros ortográficos."
        resultado = analisar_texto(texto)
        self.assertIsInstance(resultado, dict)
        self.assertIn("exemplo", resultado)

if __name__ == "__main__":
    unittest.main()
