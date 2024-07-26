# tests/test_quasi_polynomials.py
import unittest
from QuasiPolyLib import QuasiPolynomial
import sympy as sp

class TestQuasiPolynomial(unittest.TestCase):
    def test_initialization(self):
        s = sp.symbols('s')
        qp = QuasiPolynomial([(s**3, 0), (s**2 + 1, 4), (s + 6, 2)])
        expected = s**3 + sp.exp(-4*s)*(s**2 + 1) + sp.exp(-2*s)*(s + 6)
        self.assertEqual(str(qp.quasi_poly), str(expected))

    def test_evaluation(self):
        s = sp.symbols('s')
        qp = QuasiPolynomial([(s**3, 0), (s**2 + 1, 4), (s + 6, 2)])
        result = qp.evaluate(1)
        expected = 7 * sp.exp(-4) + 7 * sp.exp(-2) + 1
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()
