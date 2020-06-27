import unittest
from locker import Credentials

class LockerTest(unittest.TestCase):
    def setUp(self):
        '''
        method run before each test
        '''
        self.new_account = Credentials("instagram","linda","myPassword")
        print("setup")

    def tearDown(self):
        '''
        method run after each test
        '''
        Credentials.account_credentials = []
        print("teardown")

    def test_init(self):
        '''
        test to check for proper initialization
        '''
        self.assertEqual(self.new_account.account_name,"instagram")
        self.assertEqual(self.new_account.username,"linda")
        self.assertEqual(self.new_account.password,"myPassword")
        print("init")

    def test_save_account(self):
        '''
        test method that checks if account has been saved
        '''
        self.new_account.save_account()
        self.assertEqual(len(Credentials.account_credentials),1)
        print("save1")

    def test_save_multiple(self):
        '''
        test method to check if user can add many accounts
        '''
        self.new_account.save_account()
        another_account = Credentials("Twitter", "Bob", "Burgers123")
        another_account.save_account()
        self.assertEqual(len(Credentials.account_credentials),2)
        print("save2")
        
    def test_delete_account(self):
        '''
        test method to check if an account has been deleted
        '''
        self.new_account.save_account()
        self.new_account.delete_account()
        self.assertEqual(len(Credentials.account_credentials),0)
        print("delete")

    
    def test_password_autogenerate(self):
        '''
        '''
        self.new_account.save_account()
        another_account = Credentials("Twitter", "Bob")
        another_account.save_account()
        print(another_account.password)
        print("pas-generate")

if __name__ == "__main__":
    unittest.main()