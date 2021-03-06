from unittest import TestCase

from Main import Main

class MainTest(TestCase):
    def test_contarElementos(self):
        self.assertEqual(Main().contarElementos([""]),["0", "0", "0", "0"], "Cadena Vacia")

    def test_contarElementos_UnElemento(self):
        self.assertEqual(Main().contarElementos(["1"]), ["1", "1", "1", "1.0"], "Un Numero")

    def test_contarElementos_DosElementos(self):
        self.assertEqual(Main().contarElementos(["1","2"]), ["2","1", "2", "1.5"], "Dos Numeros")

    def test_contarElementos_NNumeros(self):
        self.assertEqual(Main().contarElementos(["1","2","3","4","5"]), ["5", "1", "5", "3.0"], "N Numeros")
