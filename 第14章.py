
# http://tinyurl.com/j9qjnep

"""
class Square:
    square_list = []
    square_list2 = []    
    
    def __init__(self, s1): 
        self.s1 = s1
        self.square_list.append(self.s1)
        self.square_list2.append(self)
         
    def __repr__(self):
        return "{} by {} by {} by {}".format(self.s1, self.s1, self.s1, self.s1,)
         
sq1 = Square(11)
sq2 = Square(12)
sq3 = Square(13)
sq4 = Square(14)


print(Square.square_list)
print(Square.square_list2)

print(sq1)
print(sq2)
print(sq3)
print(sq4)
"""


class Square:
    def __init__(self, s1): 
        self.s1 = s1

sq1 = Square(11)
sq2 = Square(12)


def Comp(p1, p2):
    return p1 is p2

co1 = Comp(sq1, sq1)
co2 = Comp(sq1, sq2)

print(sq1)
print(sq2)

print(Comp(sq1, sq2))
print(co2)    
print(Comp(sq1, sq1))
print(co1)  

"""
def compare(obj1, obj2): 
    return obj1 is obj2 

 
print(compare("a", "b")) 
print(compare("a", "a")) 
print(compare(sq1, sq2))
print(compare(sq1, sq1))
"""








"""
class Shape(): 
    def what_am_i(self): 
        print("I am a shape.") 

 

 
class Square(Shape): 
    square_list = [] 
 
 
    def __init__(self, s1): 
        self.s1 = s1 
        self.square_list.append(self) 
 
 
    def calculate_perimeter(self): 
        return self.s1 * 4 
 
 
    def what_am_i(self): 
        super().what_am_i() 
        print("I am a Square.") 
 
 
 
 
a_square = Square(29) 
print(Square.square_list) 
another_square = Square(93) 
print(Square.square_list) 
"""
"""
class Shape(): 
    def what_am_i(self): 
        print("I am a shape.") 

 

 
class Square(Shape): 
    square_list = [] 

 
    def __init__(self, s1): 
        self.s1 = s1 
        self.square_list.append(self) 
 
 
    def calculate_perimeter(self): 
        return self.s1 * 4 
 
 
    def what_am_i(self): 
        super().what_am_i() 
        print("I am a Square.") 

 
    def __repr__(self): 
        return "{} by {} by {} by {}".format(self.s1, self.s1, self.s1, self.s1) 
 
 
a_square = Square(29) 
print(a_square) 
"""



















