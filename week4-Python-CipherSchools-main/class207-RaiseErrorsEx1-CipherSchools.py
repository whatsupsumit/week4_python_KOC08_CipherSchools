# raise errors:
# not implemented error:
# abstract method:

class Animal :
    def __init__(self , name):
        self.name = name 
    
    def sound (self):
        return NotImplementedError('you have to define this method in subclass')
      
class Dog(Animal):
    def __init__(self , name , breed):
        super().__init__(name)
        self.breed=breed
        
    def sound(self):
        return 'bhow bhow'
        
class cat(Animal):
    def __init__(self, name , breed):
        super().__init(name)
        self.name = name 
        self.breed = breed
        
    def sound (self):
        return 'meow meow'    

doggy = Dog("tommy","pug")
print(doggy.sound())     
              
              
                