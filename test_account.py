import unittest
from account import Account, NotExistingAccount

class TestAccount(unittest.TestCase):
    def setUp(self):
        self.account = Account(initial_balance=100)
    
    def test_withdraw_success(self):
        self.account.withdraw(50)
        self.assertEqual(self.account.balance, 50)
    
    def test_withdraw_insufficient_funds(self):
        with self.assertRaises(ValueError):
            self.account.withdraw(150)
    
    def test_withdraw_negative_amount(self):
        with self.assertRaises(ValueError):
            self.account.withdraw(-10)

    def test_deposit_sucess(self):
        self.account.deposit(100)
        self.assertEqual(self.account.balance, 200)

    def test_deposit_negative_amount(self):
        with self.assertRaises(ValueError):
            self.account.deposit(-50)

    def test_deposit_zero_amount(self):
        with self.assertRaises(ValueError):
            self.account.deposit(0)

    def test_transfer_success(self):
        account_2 = Account(initial_balance=0)
        self.account.transfer(50, account_2)
        self.assertEqual(self.account.balance, 50)
        self.assertEqual(account_2.balance, 50)

    def test_transfer_insufficient_funds(self):
        account_2 = Account(initial_balance=0)
        with self.assertRaises(ValueError):
            self.account.transfer(150, account_2)

    def test_transfer_negative_amount(self):
        account_2 = Account(initial_balance=0)
        with self.assertRaises(ValueError):
            self.account.transfer(-50, account_2)
    
    def test_transfer_not_exist_account(self):
        account_2 = None
        with self.assertRaises(NotExistingAccount):
            self.account.transfer(50, account_2)

if __name__ == '__main__':
    unittest.main()
