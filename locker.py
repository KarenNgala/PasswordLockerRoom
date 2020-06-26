class Credentials:
    '''
    class that creates new account credentials
    '''
    credentials=[]

    def __init__(self, account_name, username, password):
        '''
        method to initialize object
        '''
        self.account_name = account_name
        self.username = username
        self.password = password
    
