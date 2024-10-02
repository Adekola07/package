class Person:
 def __init__(self, name, age):
    self.name = name
    self.age = age
 def __str__(self):
   return f"Person(name={self.name}, age={self.age})"
 def __repr__(self):
   return f"Person('{self.name}', {self.age})"
 def __eq__(self, other):
   if isinstance(other, Person):
    return self.name == other.name and self.age == other.age
    return False
# Creating Person objects
p1 = Person("Alice", 30)
p2 = Person("Bob", 25)
p3 = Person("Alice", 30)
# Using __str__ and __repr__
print(str(p1)) # Output: Person(name=Alice, age=30)
print(repr(p1)) # Output: Person('Alice', 30)
# Using __eq__
print(p1 == p2) # Output: False
print(p1 == p3) # Output: True