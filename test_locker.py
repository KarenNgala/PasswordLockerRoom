import unittest
import pyperclip
from locker import Credentials
from locker import User

class UserTest(unittest.TestCase):
    def setUp(self):
        '''
        '''
        self.new_user = User("Human", "orAmI?")
        print("//////////////////////////////")
        print("setup-user")

    def tearDown(self):
        User.data_user = []
        print("teardown-user")

    def test_init(self):
        '''
        '''
        self.assertEqual(self.new_user.owner,"Human")
        self.assertEqual(self.new_user.key, "orAmI?")
        print("init-user")

    def test_save_user(self):
        '''
        '''
        self.new_user.save_user()
        self.assertEqual(len(User.data_user),1)
        print("user saved")

    # def test_number_of_users(self):
    #     '''
    #     '''
    #     self.new_user.save_user()
    #     another_user = User("Oliver", "tToTheTwist")
    #     another_user.save_user()
        

class LockerTest(unittest.TestCase):
    def setUp(self):
        '''
        method run before each test
        '''
        self.new_account = Credentials("instagram","linda","myPassword")
        print("*****************************")
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
        another_account = Credentials("Twitter", "Bob", "Sagers")
        another_account.save_account()
        print(len(Credentials.account_credentials)) #test
        self.new_account.delete_account()
        self.assertEqual(len(Credentials.account_credentials),1)
        print(len(Credentials.account_credentials)) #test

    
    def test_password_autogenerate(self):
        '''
        '''
        self.new_account.save_account()
        another_account = Credentials("Twitter", "Bob")
        another_account.save_account()
        print("pass generate: " + another_account.password)

    def test_dislay_accounts(self):
        '''
        '''
        self.new_account.save_account()
        another_account = Credentials("Twitter","Bobby", "Brown-asf")
        another_account.save_account()
        self.assertEqual(Credentials.display_accounts(),Credentials.account_credentials)
        for acc in Credentials.account_credentials:
            print(acc.account_name)
        print("display")

    def test_search_accounts(self):
        '''
        '''
        self.new_account.save_account()
        another_account = Credentials("Twitter", "Bob", "Burgers@123")
        another_account.save_account()
        self.assertEqual(another_account.account_name,Credentials.search_accounts("Twitter"))
        print("search")


        
if __name__ == "__main__":
    unittest.main()