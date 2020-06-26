import unittest
from locker import Credentials

class LockerTest(unittest.TestCase):
    def setUp(self):
        '''
        run before each test
        '''
        self.new_account = Credentials("instagram","linda","myPassword")

    def tearDown(self):
        '''
        run after each test
        '''
        new_credentials=[]

    def test_init(self):
        '''
        test to check initialization
        '''
        self.assertEqual(self.new_account.account_name,"instagram")
        self.assertEqual(self.new_account.username,"linda")
        self.assertEqual(self.new_account.password,"myPassword")


if __name__ == "__main__":
    unittest.main()