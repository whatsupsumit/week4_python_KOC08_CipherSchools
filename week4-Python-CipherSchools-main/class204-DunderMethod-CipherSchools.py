# special magic methods/dunder methods
# operator overloading
# polymorphism- method overriding

class Phone:
    def __init__(self,brand,model, price):
        self.brand = brand 
        self.model = model
        self.price =price

    def phone_name(self):
        return f"{self.brand} {self.model}"

        # str , repr
        def __repr__(self):            
            return f"{self.brand} {self.price}"

        def __str__(self):           
            return f"{self.brand} {self.model} and price is {self.price}"
        def __len__(self):
            return len(self.phone_name())
        def __add__(self,other):
            return self.price + other.price  


# l= [1,2,3]
# print(len(l))
# t = (1,2,3)
# print(len(t))
# s ="harshit"
# print(len(s))
class Smartphone(Phone):
    def __init__ (self, brand , model , price , camera):
        super().__init__(brand, model , price)
        self.camera = camera
        
    def phone_name(self):
        return f"{self.brand} {self.model} and and price is {self.price}"    

my_phone = Phone ("nokia","1100",1000)
my_phone2 = Phone ("nokia","1600",2000)
# print(my_phone + my_phone2)
# print(str(my_phone))
# print(repr(my_phone))
# print(my_phone.__repr__())
my_smartphone = Smartphone('oneplus','5s',33000,'16MP')
print(my_smartphone.phone_name())
print(my_phone.phone_name())
print(len(my_smartphone))

