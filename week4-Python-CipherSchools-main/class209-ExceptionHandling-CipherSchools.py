# EXCEPTION HANDLING
# try except else finally

try:
    age = int(input('enter your age: '))       # 7
except ValueError:
    print('Invalid Input')
if age <18:
    print("you can't play this game.")
else:
    print("you can play this game.")     