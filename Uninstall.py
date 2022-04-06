from os import system,environ
from dotenv import load_dotenv
load_dotenv(dotenv_path='Driver/.env')
def Delete():
    password=environ.get('username')
    print('You will remove all the code :')
    password1=input('You Name :')
    if password==password1:
        system('cd ..')
        system('rmdir /q /s COPYCODEPTIT1')
        print()
    else :
        print('Wrong Password')
Delete()
