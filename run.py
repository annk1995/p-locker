#!/usr/bin/env python3.6
from user import User
from credentials import Credentials
import random

def cr_user(user_name, password):
    """
    Function to create a new user
    """
    new_user = User(user_name, password)
    return new_user

def ad_credentials(account_name, account_user_name, account_password):
    """
    Function to create a new credentials account
    """
    new_account = Credentials(account_name, account_user_name, account_password)
    return new_account

def create_user(user):
    '''
    Function to create new user
    '''
    user.create_user()

def add_credentials(credentials):
    '''
    Function to create new user credentials account
    '''
    credentials.add_credentials()

def del_credentials(name):
    '''
    Function to delete an account's credentials
    '''
    Credentials.delete_credentials(name)

def dis_all_accounts():
    '''
    Function that returns all the saved accounts and their credentials
    '''
    return Credentials.display_all_accounts()

def find_account(name):
    '''
    Function that finds an account by its account name and returns the account's credentials
    '''
    return Credentials.find_by_account(name)

def main():
    print("*"*100)
    print('                                       PASSWORD LOCKER')
    print("*"*100)
    user_name = ""
    password = ""
    print("Hello Welcome to the Password Locker. What do they name you?")
    name = input()

    print(f"Hello {name}. What would you like to do?")
    print('\n')

    while True:
        print("Use these short codes : rg - register, lg - login , ex - exit password locker ")
        print('\n')

        short_code = input().lower()

        if short_code == 'rg':
                print('\n')
                print("-"*10)
                print("--New User--")
                print("-"*10)

                print ("User Name : ")
                user_name = input()

                print("Password : ")
                password = input()

                create_user(cr_user(user_name, password)) # create and save new user.
                print ('\n')
                print(f"New User_name is:  {user_name} and password is: {password}")
                print ('\n')
                print("You may now use your username and password to og In")
                print('-'*30)


        elif short_code == 'lg':

                print("\n")
                print("-"*20)
                print("--User Login--")
                print("-"*20)

                print ("User Name :")
                login_user_name = input()

                print("Password :")
                login_password = input()

                if login_user_name == user_name and login_password == password:

                    print ('*'*50)
                    print(f"Welcome {user_name}! Login was successful")
                    print ('*'*50)

                    while True:
                        print("Use these short codes : ac - add credential's account, dc - display credentials' accounts, fc -find an account's credentials, del - delete a credentials account, lo -logout of user")
                        print('\n')
                        short_code = input().lower()

                        if short_code == 'ac':
                                print("New Credentials Account")
                                print("-"*10)

                                print ("Account name :")
                                account_name = input()

                                print("User name :")
                                account_user_name = input()

                                while True:
                                    print("Use these short codes : ty - type individual password, ag - auto generate a password")
                                    print('\n')
                                    short_code = input().lower()

                                    if short_code == 'ty':

                                        print("Password :")
                                        account_password = input()
                                        break

                                    elif short_code == 'ag':

                                        passwords = ("++notMyPassword", "p@$$w0rd", "++johnDoe++", "lostPassword")
                                        generated = passwords[random.randint(0,3)]
                                        print("-"*20)
                                        print(f"Auto generated password is {generated}")
                                        print("-"*20)
                                        print("Use these short codes : sp - select password, ga - generate another password")
                                        print('\n')
                                        short_code = input().lower()

                                        if short_code == 'sp':
                                            account_password = generated
                                            print(f"Password updated. Your password is {account_password}")
                                            break

                                        elif short_code == 'ga':
                                            generated = passwords[random.randint(0,3)]
                                            print("-"*20)
                                            print(f"Auto generated password is {generated}")
                                            print("-"*20)
                                            print("Use these short codes : sp - select password, ga - generate another password")
                                            print('\n')
                                            short_code = input().lower()

                                            if short_code == 'sp':
                                                account_password = generated
                                                print(f"Password updated. Your password is {account_password}")
                                                break

                                            elif short_code == 'ga':
                                                generated = passwords[random.randint(0,3)]
                                                print("-"*20)
                                                print(f"Auto generated password is {generated}")
                                                print("-"*20)
                                                print("Use these short codes : sp - select password, gb - go back")
                                                print('\n')
                                                short_code = input().lower()

                                                if short_code == 'sp':
                                                    account_password = generated
                                                    print(f"Password updated. Your password is {account_password}")
                                                    break

                                        else:
                                            print("I really didn't get that. Please use the short codes")
                                    else:
                                        print("I really didn't get that. Please use the short codes")


                                add_credentials(ad_credentials(account_name, account_user_name, account_password))
                                print ('-'*50)
                                print("New Account added")
                                print ('-'*50)
                                print(f"Account Name{account_name}.... User Name {account_user_name}.... Password {account_password}")
                                print ('\n')

                        elif short_code == 'del':
                                print("Enter the name of the account you want to delete")

                                deleted_account = input()
                                if del_credentials(deleted_account):
                                        del_credentials(deleted_account)

                        elif short_code == 'dc':
                                if dis_all_accounts():
                                        print("Here is a list of all your accounts and their credentials")
                                        print('\n')

                                        for account in dis_all_accounts():
                                                print(f" Account Name: {account.account_name} \n User Name: {account.account_user_name} \n Password: {account.account_password}")

                                                print('\n')
                                else:
                                        print('\n')
                                        print("You dont seem to have any accounts saved yet")
                                        print('\n')

                        elif short_code == 'fc':

                                print("Enter the name of the account you want to search for")

                                search_name = input()
                                if find_account(search_name):
                                        search_account = find_account(search_name)
                                        print(f"Account name: {search_account.account_name}")
                                        print('-'*20)

                                        print(f"User Name.......{search_account.account_user_name}")
                                        print(f"Password.......{search_account.account_password}")
                                else:
                                        print('-'*50)
                                        print("That Account does not exist")
                                        print('-'*50)

                        elif short_code == "lo":
                                print("Log Out was successful .......")
                                break
                        else:
                                print("I really didn't get that. Please use the short codes")

                else:
                    print('-'*50)
                    print(f"Login failed. Username or Password is incorrect")
                    print('-'*50)

        elif short_code == "ex":
                print("Bye, your credentials are protected! .......")
                break

        else:
                print("I really didn't get that. Please use the short codes")


if __name__ == '__main__':

    main()