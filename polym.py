class Cat:
    def _init_(self, name, age):
        self.name = name
        self.age = age
    def info(self):
        print("Iam a Cat. My name is {self.name} and i am {self.age} years old")
    def make_sound(self):
        print("Meow")
class Goat:
    def _init_(self, name, age):
        self.name = name
        self.age = age
    def info(self):
        print("Iam a Dog. My name is {self.name} and i am {self.age} years old")
    def make_sound(self):
        print("Woof")
        
    cat1 = Cat("Kitty", 6)
    goat1 = Goat("Fluty", 12) # type: ignore
    for animal in (cat1, goat1):
        animal.make_sound()
        animal.info()
        animal.make_sound()