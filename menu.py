from users import Users
import os

login_val = False

class Menu:
    
    def show ():
        print ("Welcome to SIGA")
        print ("we are happy to have you here\n")
    
    def option ():
        print ("1. Make an account")
        print ("2. Already have an account\n")
        return input ()
    
    def login_account ():
        global login_val
        Try_again = 1
        while (Try_again == 1):
            username_val = False
            password_val = False
            os.system ('cls')
            print ("It's time to login: ")
            key = input("User: ")
            for x in Users:
                if (x == key):
                    username_val = True
            value = input("Password: ")
            for y in Users.values():
                if (y == value):
                    password_val = True

            if (username_val and password_val):
                login_val = True
                Try_again = 0
            else:
                print ("\nTry again?")
                print ("1. Yes")
                print ("2. Not")
                Try_again = int (input())
            
    
    def new_account (): 
        account_validation = False
        while (account_validation == False):
            os.system ('cls')  
            print ("create an account is easy")
            key = input("Enter your user name: ")
            account_validation = True
            for x in Users:
                if (x == key):
                    account_validation == False

        value = input ("Enter your password: \n")
        Users [key] = value
        print ("\nYour account has been created!\n")
        print ("Enter to login in your account")
        input ()
        Menu.login_account()