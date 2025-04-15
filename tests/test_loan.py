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
        expected_balance = [
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
        self.assertEqual(expected_balance,
                         [amort['balance'] for amort in loan.amortization])

    def test_loan_2(self):
        loan = Loan(principal=100000, term=12, rate=5.2)
        expected_payment = 8569.92
        expected_balance = [
            100000.00,
            91863.42,
            83691.58,
            75484.32,
            67241.51,
            58962.97,
            50648.56,
            42298.12,
            33911.50,
            25488.53,
            17029.06,
            8532.94,
            0.00,
        ]
        result = [amort['principal'] for amort in loan.amortization]
        self.maxDiff = None
        self.assertAlmostEqual(expected_payment, loan.payment, 2)
        self.assertEqual(len(expected_principal), len(result))
        for month in zip(expected_principal, result):
            self.assertAlmostEqual(month[0], month[1], 2)


# Aug 2021	$8,569.92	$8,136.58	$433.33	$433.33	        $91,863.42
# Sep 2021	$8,569.92	$8,171.84	$398.07	$831.41	        $83,691.58
# Oct 2021	$8,569.92	$8,207.25	$362.66	$1,194.07	$75,484.32
# Nov 2021	$8,569.92	$8,242.82	$327.10	$1,521.17	$67,241.51
# Dec 2021	$8,569.92	$8,278.54	$291.38	$1,812.55	$58,962.97
# Jan 2022	$8,569.92	$8,314.41	$255.51	$2,068.06	$50,648.56
# Feb 2022	$8,569.92	$8,350.44	$219.48	$2,287.53	$42,298.12
# Mar 2022	$8,569.92	$8,386.62	$183.29	$2,470.83	$33,911.50
# Apr 2022	$8,569.92	$8,422.97	$146.95	$2,617.78	$25,488.53
# May 2022	$8,569.92	$8,459.47	$110.45	$2,728.23	$17,029.06
# Jun 2022	$8,569.92	$8,496.12	$73.79	$2,802.02	$8,532.94
# Jul 2022	$8,569.92	$8,532.94	$36.98	$2,838.99	$0.00      
