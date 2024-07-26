# tests/test_quasi_polynomials.py
import unittest
from QuasiPolyLib import QuasiPolynomial

class TestQuasiPolynomial(unittest.TestCase):
    def test_initialization(self):
        s = sp.symbols('s')
        qp = QuasiPolynomial([(s**3, 0), (s**2 + 1, 4), (s + 6, 2)])
        print("Quasi-Polynomial:", qp)
        print("Evaluated at s=1:", qp.evaluate(1))
        print("Derivative:", qp.derivative())
        print("Simplified:", qp.simplify())

if __name__ == '__main__':
    unittest.main()
