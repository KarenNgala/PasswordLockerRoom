#!/usr/bin/python3

from locker import Credentials
from locker import User

# new_account is an instance of Credentials class. Contains details for one account
# new_user is an instance of User class. Contains username and password of lock room user

def create_user(lock_owner, lock_key):
    '''
    '''
    new_user = User(lock_owner, lock_key)
    return new_user

def save_user(data):
    '''
    '''
    data.save_user()

def create_account(account, u_name, passwd):
    '''
    '''
    new_account = Credentials(account, u_name, passwd)
    return new_account

def save_accounts(credentials):
    '''
    '''
    credentials.save_account()

def delete_accounts(credentials):
    '''
    '''
    credentials.delete_account()

def search_accounts(search):
    '''
    '''
    return Credentials.search_accounts(search)

def generate_password():
    '''
    '''
    random_password = Credentials.password_generate()
    return random_password

def display_account():
    '''
    '''
    return Credentials.display_accounts()


def main(): 
    print(' _               _               ____                       ')
    print('| |    ___   ___| | _____ _ __  |  _ \ ___   ___  _ __ ___  ')
    print("| |   / _ \ / __| |/ / _ \ '__| | (_) / _ \ / _ \| '_ ` _ \ ")
    print('| |__| (_) | (__|   <  __/ |    |  _ < (_) | (_) | | | | | |')
    print('|_____\___/ \___|_|\_\___|_|    |_| \_\___/ \___/|_| |_| |_|')

    print("\nHello and welcome!")
    print("\n 1. Create an account \n 2. Exit app")
    option = input()

    if option == '1':
        print("Enter your name")
        lock_owner = input()
        if not lock_owner:
            print("You must type something in")
        else:
            print("Enter a password")
            lock_key = input()
            if not lock_key:
                print("You must type something in")
            else:
                save_user(create_user(lock_owner, lock_key))
                print("-"*10)
                print(f"{lock_owner}, please enter your password again to login.")
                confirm = input()
                if confirm == lock_key:
                    print("\n You are successfully logged in!")
                    while True:
                        print("-"*10)
                        print("Use these short codes : \n \t\t aa - Add an account using your own password \n \t\t ga - Generate a password for your new account \n \t\t da - display saved accounts \n \t\t sa - Search for an account \n \t\t ex - Exit the locker room ")
                        short_code = input().lower()

                        if short_code == 'aa':
                            print("-"*10)
                            print("Enter an existing account")
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
                            print("-"*10)
                            print("Account name ....(eg: facebook)")
                            account = input()
                            print("Username ...")
                            u_name = input()
                            print("...........")
                            passwd = generate_password()
                            save_accounts(create_account(account, u_name, passwd))
                            print ('Your account has been created successfully!\n')
                            print(f"New account: {account} \n Username: {u_name} --- Password:{passwd}")
                            print ('\n')

                        elif short_code == 'da':
                            print("-"*10)
                            if display_account() != []:
                                print("\nHere is a list of all your accounts:\n")
                                for item in display_account():
                                    print(item.account_name +"\t --> "+ item.username +"\t --> "+ item.password)
                            else:
                                print("\n You do not have any accounts saved \n")

                        elif short_code == 'sa':
                            print("-"*10)
                            print("\n Enter an account type to search. eg:Facebook\n")
                            search = input()
                            if search_accounts(search):
                                found = search_accounts(search)
                                print("\n Here's what we've found:\n")
                                print(found.account_name +"\t"+ found.username +"\t"+ found.password)
                        
                        elif short_code == "ex":
                            print("-"*10)
                            print(f"Have a lovely day, {lock_owner}")
                            break
                        else:
                            print("-"*10)
                            print("\nInvalid short code. Please take your time to read them, and try again\n")
                else:
                    print("-"*10)
                    print("\nIncorrect password. Try again")
    elif option == '2':
        print("-"*10)
        print(f"\nHave a lovely day, {lock_owner}")
    else:
        print("-"*10)
        print("\nInvalid option. Please try again later")

if __name__ == "__main__":
    main()