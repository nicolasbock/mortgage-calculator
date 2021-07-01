import unittest

from mortgage_calculator.loan import Loan


class TestLoan(unittest.TestCase):

    def test_constructor(self):
        loan = Loan(principal=100000, term=20, rate=4.3)
        self.assertEqual(100000, loan.principal)
        self.assertEqual(20, loan.term)
        self.assertEqual(4.3, loan.rate)
