from os import system
def Delete():
    password='123'
    print('You will remove all the code :')
    password1=input('You Password :')
    if password==password1:
        # system('del .gitignore')
        # system('del  main.py')
        # system('del  README.md')
        # system('del  Libary.py')
        # system('rmdir /q /s Driver')
        # system('del  Uninstall.py')
        system('rmdir /q /s __pycache__')
    else :
        print('Wrong Password')
Delete()
