# polymorphism means  same method name, different behavior
# it allows flexibility: different classes can define the same method but act differently
# achieved by method overriding or duck typing

# Example:

class dog: 
     def speak(self): 
         return "woof!"
     
class cat:
    def speak(self):
        return "Meow!"

class cow:
    def speak(self):
        return "Moo!"
     
     
def animalsound(animal):
    print(animal.speak())
    
Dog = dog()
Cat = cat()
Cow = cow()

animalsound(Dog)
animalsound(Cat)
animalsound(Cow)

# OUTPUT: 

""" 
    Woof!
    Meow!
    Moo!
"""