import unittest
import pyperclip
from locker import Credentials
from locker import User

class UserTest(unittest.TestCase):
    def setUp(self):
        '''
        method run before each user test
        '''
        self.new_user = User("Human", "orAmI?")

    def tearDown(self):
        '''
        method called after each user test
        '''
        User.data_user = []

    def test_init(self):
        '''
        test method to check if user class is initialized correctly
        '''
        self.assertEqual(self.new_user.owner,"Human")
        self.assertEqual(self.new_user.key, "orAmI?")
        
    def test_save_user(self):
        '''
        test method to test if user has been saved into class list
        '''
        self.new_user.save_user()
        self.assertEqual(len(User.data_user),1)


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
        Credentials.account_credentials = []

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

    def test_save_multiple(self):
        '''
        test method to check if user can add many accounts
        '''
        self.new_account.save_account()
        another_account = Credentials("Twitter", "Bob", "Burgers123")
        another_account.save_account()
        self.assertEqual(len(Credentials.account_credentials),2)
        
    def test_delete_account(self):
        '''
        test method to check if an account has been deleted
        '''
        self.new_account.save_account()
        another_account = Credentials("Twitter", "Bob", "Sagers")
        another_account.save_account()
        self.new_account.delete_account()
        self.assertEqual(len(Credentials.account_credentials),1)
    
    def test_password_autogenerate(self):
        '''
        test method to test auto generation of passwords
        '''
        self.new_account.save_account()
        another_account = Credentials("Twitter", "Bob")
        another_account.save_account()

    def test_dislay_accounts(self):
        '''
        test method to check displaying of accounts
        '''
        self.new_account.save_account()
        another_account = Credentials("Twitter","Bobby", "Brown-asf")
        another_account.save_account()
        self.assertEqual(Credentials.display_accounts(),Credentials.account_credentials)

    def test_search_accounts(self):
        '''
        test method to test search functionality
        '''
        self.new_account.save_account()
        another_account = Credentials("Twitter", "Bob", "Burgers@123")
        another_account.save_account()
        self.assertEqual(another_account,Credentials.search_accounts("Twitter"))


if __name__ == "__main__":
    unittest.main()