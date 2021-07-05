import unittest

from mortgage_calculator.loan import Loan


class TestLoan(unittest.TestCase):

    def test_constructor(self):
        loan = Loan(principal=100000, term=20, rate=4.3)
        self.assertEqual(100000, loan.principal)
        self.assertEqual(20, loan.term)
        self.assertEqual(4.3, loan.rate_percent)
        self.assertEqual(0.043, loan.rate)

    def test_negative_rate(self):
        with self.assertRaisesRegex(Exception, "The rate cannot be negative"):
            loan = Loan(principal=100000, term=20, rate=-1)

    def test_loan_1(self):
        loan = Loan(principal=100000, term=10, rate=0)
        expected_principal = [
            100000.0,
            90000.0,
            80000.0,
            70000.0,
            60000.0,
            50000.0,
            40000.0,
            30000.0,
            20000.0,
            10000.0,
            0.0,
        ]
        self.assertEqual(expected_principal,
                         [amort['principal'] for amort in loan.amortization])

    def test_loan_2(self):
        loan = Loan(principal=100000, term=10, rate=5)
        expected_principal = [
            100000.0,
            92049.5425,
            83701.5621,
            74936.1827,
            65732.5344,
            56068.7036,
            45921.6813,
            35267.3079,
            24080.2158,
            12333.769,
            0.0,
        ]
        self.assertAmostEqual(expected_principal,
                              [amort['principal'] for amort in loan.amortization])
