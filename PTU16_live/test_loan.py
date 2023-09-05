from PTU16_live.loan import Loan
import unittest


class TestLoan1(unittest.TestCase):
    printed = False

    def setUp(self) -> None:
        self.loan = Loan(11000, 7, 12, 1000)
        self.loan.print_loan_info()
        self.loan.print_monthly_payments()

    def test_principal(self):
        self.assertAlmostEqual(self.loan.principal, 10000, 2)

    def test_interest(self):
        self.assertAlmostEqual(self.loan.increase, 383.21, 2)

    def test_totals(self):
        self.assertAlmostEqual(self.loan.loan_total, 11383.21, 2)
        self.assertAlmostEqual(self.loan.repayable, 10383.21, 2)

    def test_monthly(self):
        self.assertAlmostEqual(self.loan.monthly, 865.26, 2)

    def test_loan_balance(self):
        self.assertAlmostEqual(self.loan.repayable, sum(self.loan.payments))


class TestLoan2(unittest.TestCase):
    def setUp(self) -> None:
        self.loan = Loan(63000, 5, 60, 12600)
        self.loan.print_loan_info()
        self.loan.print_monthly_payments()

    def test_principal(self):
        self.assertAlmostEqual(self.loan.principal, 50400, 3)

    def test_interest(self):
        self.assertAlmostEqual(self.loan.increase, 6666.61, 3)

    def test_totals(self):
        self.assertAlmostEqual(self.loan.loan_total, 69666.61, 3)
        self.assertAlmostEqual(self.loan.repayable, 57066.61, 3)

    def test_monthly(self):
        self.assertAlmostEqual(self.loan.monthly, 951.11, 3)

    def test_loan_balance(self):
        self.assertAlmostEqual(self.loan.repayable, sum(self.loan.payments))
