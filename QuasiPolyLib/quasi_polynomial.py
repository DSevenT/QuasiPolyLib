import sympy as sp

class QuasiPolynomial:
    def __init__(self, terms):
        """
        Initialize the QuasiPolynomial with terms.

        :param terms: List of tuples where each tuple contains a polynomial and a delay.
                      The polynomial should be a SymPy expression in terms of 's'.
                      Example: [(s**2 + 1, 4), (s + 6, 2)]
        """
        self.s = sp.symbols('s')
        self.terms = terms
        self.quasi_poly = self._create_quasi_polynomial()

    def _create_quasi_polynomial(self):
        """
        Construct the quasi-polynomial using symbolic s.

        :return: A symbolic representation of the quasi-polynomial.
        """
        quasi_poly = 0
        for poly, tau in self.terms:
            quasi_poly += poly * sp.exp(-tau * self.s)
        return quasi_poly

    def __repr__(self):
        return f"QuasiPolynomial({self.quasi_poly})"

    def evaluate(self, s_value):
        """
        Evaluate the quasi-polynomial at a specific value of s.

        :param s_value: The value at which to evaluate the quasi-polynomial.
        :return: The evaluated value.
        """
        return self.quasi_poly.subs(self.s, s_value)

    def derivative(self):
        """
        Compute the derivative of the quasi-polynomial with respect to s.

        :return: The derivative of the quasi-polynomial.
        """
        return sp.diff(self.quasi_poly, self.s)

    def simplify(self):
        """
        Simplify the quasi-polynomial expression.

        :return: A simplified version of the quasi-polynomial.
        """
        return sp.simplify(self.quasi_poly)

# Example usage:
if __name__ == "__main__":
    s = sp.symbols('s')
    qp = QuasiPolynomial([(s**3, 0), (s**2 + 1, 4), (s + 6, 2)])
    print("Quasi-Polynomial:", qp)
    print("Evaluated at s=1:", qp.evaluate(1))
    print("Derivative:", qp.derivative())
    print("Simplified:", qp.simplify())
