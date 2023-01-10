# python custom exception
# q : why custom exception 
# a: to increase the readability of code
# example


class nameTooShortError(ValueError):
    pass
def validate(name):
    if len(name)<8:
        raise ValueError("name is too short.")
username = input("enter yur name :") 
validate(username) 
print(f"hello {username}")  
        