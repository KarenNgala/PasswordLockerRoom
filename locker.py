class Credentials:
    '''
    class that creates new account credentials
    '''
    account_credentials=[] #list of accounts

    def __init__(self, account_name, username, password):
        '''
        method to initialize account object
        '''
        self.account_name = account_name
        self.username = username
        self.password = password
    
    # new_account is an instance of Credentials class. Contains details for one account

    def save_account(self):
        '''
        method to save account object
        '''
        self.account_credentials.append(Credentials)
