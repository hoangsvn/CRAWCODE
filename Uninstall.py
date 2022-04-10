from os import system
def Delete():
    password='123'
    print('You will remove all the code :')
    password1=input('You Password :')
    if password==password1:
        system('del  .env')
        system('del .gitignore')
        system('del  chromedriver.exe')
        system('del  Libary.py')
        system('del  main.py')
        system('del  main1.py')
        system('del  README.md')
        system('rmdir /q /s __pycache__')
        system('del  Uninstall.py')
    else :
        print('Wrong Password')
Delete()
