from os import system
try:
    system('git status')
    system('git add .')
    system('git commit -m "hoang"')
    system('git push')
    
except:
    print('ERROR')