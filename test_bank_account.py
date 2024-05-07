from unittest import TestCase

from bank_account import BankAccount
from errors.insufficient_fund_error import InsufficientFundError

class TestBankAccount(TestCase):
  def setUp(self):
    self.bank_account = BankAccount(100)

  def test_deposit(self):
    self.bank_account.deposit(100)
    self.assertEqual(self.bank_account.balance, 200)

  def test_withdraw(self):
    self.bank_account.withdraw(50)
    self.assertEqual(self.bank_account.balance, 50)

  def tearDown(self):
    self.bank_account = None
