import os

# os.getcwd()
# print(os.getcwd())
# os.mkdir('movies')
# if os.path.exists('movies'):
#     print('already exists')
# else:
#     os.mkdir('movies')

open ('file.txt',"a").close()
print(os.listdir())

for item in os.listdir():
    path = os.path.join(os.getcwd(),item)
    print(path)
