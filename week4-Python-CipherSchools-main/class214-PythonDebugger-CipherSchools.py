import pdb 
# import pdb module 
# module Python file contains useful classes and functions wrote by developer


# according to wikipedia debugging is the process of finding and resolving defects or problems within 
# a computer program that prevent correct operation of computer software or a system.

# why debugging
# 1.) our program is not running and causing unexpected errors.
# 2.) our program is working fine but not working the same way we want.


# steps for debugging :
# 1.) set trace
# 2.) execute code line by line.

pdb.set_trace()
name = input("please type your name: ")
age = input('please type your age: ')
print(f"please type your age : ")
age2 = age+5
print(f"{name} you will be {age2} in next five years")


# l 
# c 
# q
