
# http://tinyurl.com/hz9qdh3

"""
# 4.

class Horse:
    def __init__(self, name, breed, owner):
        self.name = name
        self.bred = breed
        self.ower = owner

class Raider:
    def __init__(self, name):
        self.name = name

ra1 = Raider("Mick Jagger")
ho1 = Horse("Stanley", "Bulldog", ra1)

print(ho1.ower.name)
"""

# 3.

class Shape:
    #def __init__(self):
    #    pass

    def what_am_i(self):
        print("I am a shape")
        
sh1 = Shape()
sh1.what_am_i()

class Rectangle(Shape): 
    def __init__(self, r1, r2): 
        self.r1 = r1 
        self.r2 = r2 
 
    def calculate_perimeter(self):
        return (self.r1 + self.r2) * 2
         
re1 = Rectangle(10, 13) 
print(re1.calculate_perimeter()) 
re1.what_am_i()

class Square(Shape): 
    def __init__(self, s1): 
        self.s1 = s1
         
    def calculate_perimeter(self):
        return self.s1 * 4
         
sq1 = Square(11) 
print(sq1.calculate_perimeter()) 
sq1.what_am_i()


"""
# 2.

class Square: 
    def __init__(self, s1): 
        self.len = s1
         
    def calculate_perimeter(self):
        return self.len * 4
         
    def change_size(self, d):
        self.v = d
        # self.len = self.len + self.v
        self.len += self.v


sq1 = Square(11) 
print(sq1.calculate_perimeter()) 

sq1.change_size(2) 
print(sq1.calculate_perimeter()) 

sq1.change_size(-4) 
print(sq1.calculate_perimeter()) 


# 1.

class Rectangle: 
    def __init__(self, r1, r2): 
        self.r1 = r1 
        self.r2 = r2 
 
    def calculate_perimeter(self):
        return (self.r1 + self.r2) * 2
         
re1 = Rectangle(10, 13) 
print(re1.calculate_perimeter()) 

class Square: 
    def __init__(self, s1): 
        self.s1 = s1
         
    def calculate_perimeter(self):
        return self.s1 * 4
         
sq1 = Square(11) 
print(sq1.calculate_perimeter()) 


"""
