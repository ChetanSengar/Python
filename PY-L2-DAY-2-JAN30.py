

class dummy:
   def __init__(self):
       print  ('in __init__()')

   def __del__(self):
       print  ('in __del__()')


def   f2():
   a = dummy()
   b = a
   c = b
   print ('in f2 calling del a')
   del a
   print ('in f2 after calling del a')
   
   print ('in f2 calling del c')
   del c
   print ('in f2 after calling del c')
   
   print ('in f2 calling del b')
   del b
   print ('in f2 after calling del b')
   
   print ('return from f2()')



class Point:
     def   __init__(self, tx, ty):
             self.x = tx
             self.y = ty
     def getx(self): return self.x
     def gety(self): return self.y
     def setx(self,tx): self.x = tx
     def sety(self,ty): self.y = ty
     """
     def  __repr__(self):
           return "".join(["RPoint(", str(self.x),
                    ",", str(self.y), ")"])

     def  __str__(self):
           return "".join(["SPoint(", str(self.x),
                     ",", str(self.y), ")"])

     """
     
def test_Point():
    p1 = Point(1,5)
    p2 = Point(3,10)
    print ('p1 -', p1)
    print ('p2 -', p2)
    p1.setx(10)
    p1.sety(20)
    print ('p1 -', p1)
    print('********')
    s1 = str(p1)
    print(s1)
    
    
class Stack:
   def __init__(self):
     self.stk=[]

   def push(self,v):
     self.stk.append(v)

   def pop(self):
      if len(self.stk) == 0:
          raise RuntimeError("stack empty")
      else:
         return self.stk.pop()

def POP(s):
    try:
        print (s.pop())
    except Exception as e:
      print (e)

def test_stack():
    try:
      s = Stack();
      s.push(10)
      s.push(20)
      print (s.pop())
      print (s.pop())
      print (s.pop())  # triggered exception
      s.push(100)
      s.push(200)
      print (s.pop())
    except Exception as e:
      print (e)


def test_stack2():
    try:
      s = Stack();
      s.push(10)
      s.push(20)
      POP(s)
      POP(s)
      POP(s)
      POP(s)
      s.push(100)
      s.push(200)
      POP(s)
    except Exception as e:
      print (e)

#test_stack2()



##############################


class Dummy:
   count = 0
   
   def __init__(self):
      #global count
      Dummy.count += 1

   def __del__(self):
      Dummy.count -= 1

   def get_count(self):
      #global count
      return Dummy.count

def test_dummy():

    d1 = Dummy()
    print(d1.get_count())

    d2 = Dummy()
    print(d2.get_count())
    
    if False:
      d3 = Dummy()
      print(d3.get_count())
      d4 = Dummy()
      print(d4.get_count())
    else:
      d5 = Dummy()
      print(d5.get_count())
        
      
    print(d2.get_count())
      
    
"""

t1 = Dummy()
print(t1.get_count())
test_dummy()
t2 = Dummy()
print(t2.get_count())
"""

###############################


class INT:
    def __init__(self, v):
        self.__v = v
        
    def __add__(self, rhs):
        return INT(self.__v + rhs.__v)
    
    def __iadd__(self, rhs):
        self.__v += rhs.__v
        return self

    def __gt__(self, t):
        return self.__v > t.__v       
        
    def __str__(self):
        return str(self.__v)
      

def test_INT():
    x = INT(3)
    y = INT(5)
    print(x > y)
    z =  x+y
    print('x = ', x)
    print('y = ', y)
    print('z = ', z)
    
    z += x
    print('z = ', z)
    
    print (x == y)
    x = y
    print(x > y)
    print('x = ', x)
    print('y = ', y)
    y = INT(2)
    print('x = ', x)
    print('y = ', y)
    print('--------')
    print(x > y)

    

test_INT()



