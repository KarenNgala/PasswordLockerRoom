import unittest
from locker import Credentials

class LockerTest(unittest.TestCase):
    def setUp(self):
        '''
        method run before each test
        '''
        self.new_account = Credentials("instagram","linda","myPassword")

    def tearDown(self):
        '''
        method run after each test
        '''
        self.new_account = []

    def test_init(self):
        '''
        test to check for proper initialization
        '''
        self.assertEqual(self.new_account.account_name,"instagram")
        self.assertEqual(self.new_account.username,"linda")
        self.assertEqual(self.new_account.password,"myPassword")

    def test_save_account(self):
        '''
        test method that checks if account has been saved
        '''
        self.new_account.save_account()
        self.assertEqual(len(Credentials.account_credentials),1)

if __name__ == "__main__":
    unittest.main()