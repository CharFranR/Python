from menu import Menu
from users import Users
import os 

def main ():
    Menu.show ()
    login ()
    
def login ():
    if (Menu.option() == "1"):
        Menu.new_account () 
    else:
        Menu.login_account ()

if __name__ == "__main__":
    main()