from os import system
try:
    system('git status')
    system('git add .')
    A=input('Nhap commit :').strip()
    system(f'git commit -m "{A}"')
    system('git push')
except:
    print('ERROR ==> git pull')