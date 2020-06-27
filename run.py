#!/usr/bin/python3

from locker import Credentials

# new_account is an instance of Credentials class. Contains details for one account

def create_account(account, u_name, passwd):
    '''
    '''
    new_account = Credentials(account, u_name, passwd)
    return new_account

def save_accounts(Credentials):
    '''
    '''
    Credentials.save_account()

def delete_accounts(Credentials):
    '''
    '''
    Credentials.delete_account()

def generate_password():
    '''
    '''
    random_password = Credentials.password_generate()
    return random_password


def main():
    print("Hello, welcome to your passwords' locker room. What is your name?")
    human = input()
    print(f" \n Hello {human}. What would you like to do today? \n")

    while True:
        print("Use these short codes : \n \t\t aa - Add an account using your own password \n \t\t ga - Let us generate a password for new account \n \t\t ex - Exit the locker room ")
        short_code = input().lower()

        if short_code == 'aa':
            print("Enter an existing account")
            print("-"*10)
            print("Account name ....(eg: facebook)")
            account = input()
            print("Username ...")
            u_name = input()
            print("Password ...")
            passwd = input()
            save_accounts(create_account(account, u_name, passwd))
            print ('\n')
            print(f"New account: {account} added \n Username: {u_name} --- Password:{passwd}")
            print ('\n')
        elif short_code == 'ga':
            print("Enter an existing account")
            print("-"*10)
            print("Account name ....(eg: facebook)")
            account = input()
            print("Username ...")
            u_name = input()
            print("Password ...")
            passwd = generate_password()
            save_accounts(create_account(account, u_name, passwd))
            print ('Your account has been created successfully!\n')
            print(f"New account: {account} \n Username: {u_name} --- Password:{passwd}")
            print ('\n')
        elif short_code == "ex":
            print(f"Have a lovely day, {human}")
            break
        else:
            print("Invalid short code. Please take your time to read them, and try again")

if __name__ == "__main__":
    main()