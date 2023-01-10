# read file
# open function
# read method
# seek method
# tell method
# readline method
# readlines method
# close method


f = open("class214-PythonDebugger-cipherSchools.py")
# print(f'cursor position- {f.tell()}')       
# print(f.read())
# print(f'cursor position- {f.tell()}')   # OR f.tell()
# print('before seek method')
# f.seek(0)
# print('after seek method')
# print()
print(f.readline())
f.close()