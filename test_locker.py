import unittest
from locker import Credentials

class LockerTest(unittest.TestCase):
    def setUp(self):
        '''
        run before each test
        '''
        self.new_account = Credentials("instagram","linda","myPassword")
        print("setup")

    def tearDown(self):
        '''
        run after each test
        '''
        self.new_account = []
        print("teardown")

    def test_init(self):
        '''
        test to check initialization
        '''
        self.assertEqual(self.new_account.account_name,"instagram")
        self.assertEqual(self.new_account.username,"linda")
        self.assertEqual(self.new_account.password,"myPassword")
        print("setup")


if __name__ == "__main__":
    unittest.main()