import unittest

from calculator import *

class CalculatorTest(unittest.TestCase):
    def test_suma_dos_numeros(self):
        calc = Calculator(5, 10)
        self.assertEqual(15, calc.suma())

    def test_resta_dos_numeros(self):
        calc = Calculator(19, 8)
        self.assertEqual(11, calc.resta())

    def test_multiplicacion_dos_numeros(self):
        calc = Calculator(9, 9)
        self.assertEqual(81, calc.multiplicacion())

    def test_division_dos_numeros(self):
        calc = Calculator(8, 4)
        self.assertEqual(2, calc.division())

    def test_potencia_dos_numeros(self):
        calc = Calculator(2, 3)
        self.assertEqual(8, calc.potencia())

    def test_raiz_dos_numeros(self):
        calc = Calculator(9, 3)
        self.assertEqual(3, calc.raiz())

    def test_division_numero_negativo(self):
        calc = Calculator(8, 0)
        self.assertEqual('No se puede dividir entre cero', calc.division())

    def test_raiz_numero_negativo(self):
        calc = Calculator(-9, 2)
        self.assertEqual('No se puede sacar raiz a un numero negativo', calc.raiz())

if __name__ == "__main__":
    unittest.main()