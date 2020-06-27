import random
class Credentials:
    '''
    class that creates new account credentials
    '''
    account_credentials=[] #list of accounts
    user = []

    def __init__(self, account_name, username, password = None):
        '''
        method to initialize account object
        '''
        self.account_name = account_name
        self.username = username
        self.password = password if password else Credentials.password_generate()
    
    def save_account(self):
        '''
        method to save account object
        '''
        self.account_credentials.append(self)

    def delete_account(self):
        '''
        method to delete an account
        '''
        self.account_credentials.remove(self)

    @classmethod
    def password_generate(cls):
        '''
        '''
        password_length = 8
        possible_characters = "@abcdefghijklmnopqrstuvwxyz-1234567890&ABCDEFGHIJKLMNOPQRSTUVWXYZ!" 
        random_character = [random.choice(possible_characters) for i in range(password_length)]
        auto_password = "".join(random_character)
        return auto_password

    @classmethod
    def display_accounts(cls):
        '''
        '''
        return cls.account_credentials

