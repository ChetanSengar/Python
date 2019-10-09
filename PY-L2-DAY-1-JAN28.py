
"""

python has no keywords like
    public / private
    
    to specifiy class members access 
    
by default, all class members are accessible
outside the class

how to restrict - 
   prefix class member with __.

   a class member with __ prefix is
   considered as private.


"""



class msg:
   # define constructor
   def __init__(self):
       self.__txt = ""
       
   def  set(self,s):   #define member method set
       self.__txt=s
       
   #add print function
   def print(self):
       print ('['+self.__txt+']')
       
   def __str__(self):
       #this should return a string
       return '{'+self.__txt+'}'
       

m = msg()
m.set("hello")
#print(m.__txt)  --> can't do this
m.print()  ## calls print member function
print(m)   ## global lib fn print() called


m.set("world")
#print(m.__txt)
m.print()

print ("---m2---")
m2 = msg()
#print(m2.__txt)
m.print()
m2.set("WORLD")
#print(m2.__txt)
m.print()
m2.__txt = "NEW TEXT"
#print(m2.__txt)
m.print()


class MSG:
   # define constructor
   def __init__(self, txtval):
       self.txt = txtval
       
   def  set(self,s):   #define member method set
       self.txt=s
       
 

   def concat_msg(self, msgobj):
       self.txt = self.txt + msgobj.txt

   def concat_txt(self, s):
       self.txt = self.txt + s
       
   def concat(self, *params):
       print(params)
       for rhs in params:
           if isinstance(rhs, str): # rhs is a string
                self.txt = self.txt + rhs
           elif isinstance(rhs, MSG):  # rhs is MSG type
                self.txt = self.txt + rhs.txt                
           elif isinstance(rhs, int):  # rhs is int  type
                self.txt = self.txt + str(rhs)
           else:
                 print('invalid type for rhs - ', rhs)
       
       
def test_msg():
    print ("---m3---")
    m3= MSG("python")  # ==> msg(m3, "python")
    print(m2.txt)
    m3.set("PYTHON")
    print(m3.txt)
    
    m3.concat("PROGRAMMING")
    print(m3.txt)
    
    m4 = MSG("SCRIPTING")
    
    print('------------m3 + m4 ------')
    m3.set("PYTHON")
    print(m3.txt)
    m3.concat(3.6)
    print(m3.txt)
    m3.concat(m4)
    print(m3.txt)


def test_msg2():
    print('-------in test_msg2() ---------')
    dt = MSG('program')
    print(dt.txt)
    dt.concat(' on ')
    print(dt.txt)
    dt.concat(28, 'Jan', 2019)
    print(dt.txt)
    
    dt.txt = 'something'
    print(dt.txt)
    
    


#############################
"""
    1. every class method takes self
       as mandatory argument
    2. self is he first arg of a class method
        
""" 

class Book:
    def __init__(self,title, auth, year, price):
        self.title = title    # introduce title as member
        self.author = auth    
        self.year = year
        self.price = price
        
    def print(self):  
        print(self.title + self.author, + self.year + self.price)
        
        
    
def test_Book():
    bk1 = Book('Intro to Python', 'xyz', 2018, 127.5)
    bk1.print()



#test_msg2()
    
class Point:
   def __init__(self, x, y):
       self.__x = x
       self.__y = y
    
   def __str__(self):
      return "("+str(self.__x)+','+str(self.__y)+')'
  
   def setx(self, val):
      self.__x = val
      
   def sety(self, val):
      self.__y = val
      
   def getx(self):
       return self.__x
        
def test_Point():
  print('----- begin test_Point ---------')
  p1 = Point(1,5)
  p2 = Point(10,20)
  print(p1)
  print(p2)
  p1.setx(3)
  p2.sety(30)
  print(p1)
  print(p2)
  print('p2.x = ', p2.getx())
  print('----- end test_Point ---------')

class Point2:
   def __init__(self, x, y, sep):
       self.__x = x
       self.__y = y
       self.__sep = sep
    
   def __str__(self):
      return "("+str(self.__x)+self.__sep+str(self.__y)+')'
  
   def setx(self, val):
      self.__x = val
      
   def sety(self, val):
      self.__y = val
      
   def getx(self):
       return self.__x 

def test_Point2():
  print('----- begin test_Point ---------')
  p1 = Point2(1,5,',')
  p2 = Point2(10,20, '-')
  print(p1)
  print(p2)
  p1.setx(3)
  p2.sety(30)
  print(p1)
  print(p2)
  print('p2.x = ', p2.getx())
  print('----- end test_Point ---------')



class Point3:
   """
   # seperator is configurable 
   # but not per object / instance
   #  only for the class
   
   all instance-level members are introduced
        in __init__
        
   all class level members are introduced 
       outside __init__
   
   """
   
   """ 
   __sep is for the class, shared by all
          instances of the class
          
   also, set_sep() is for the class

   so, these 2 are static members
   
      __sep --> static data member
      
      __set_sep()  --> static member function
   
   """
   __sep = ','   ## no self. 
   
   count = 0     ## counnt of instances
   

   @staticmethod
   def set_sep(ch_sep):
       Point3.__sep = ch_sep
   
   @staticmethod
   def getcount():
       return Point3.count
   
   def __init__(self, x, y):
       self.__x = x
       self.__y = y
       Point3.count += 1
    
   def __str__(self):
      return "("+str(self.__x)+Point3.__sep+str(self.__y)+')'
  
   def setx(self, val):
      self.__x = val
      
   def sety(self, val):
      self.__y = val
      
   def getx(self):
       return self.__x 

def test_Point3():
  print('----- begin test_Point3 ---------')
  print('object count - ', Point3.getcount())
  p1 = Point3(1,5)
  print('object count - ', Point3.getcount())
  
  p2 = Point3(10,20)
  print('object count - ', Point3.getcount())
  
  
  print(p1)
  print(p2)
  p1.setx(3)
  p2.sety(30)
  print(p1)
  print(p2)
  Point3.set_sep('%')
  print(p1)
  print(p2)
  print('p2.x = ', p2.getx())
  print('----- end test_Point3 ---------')

test_Point3()







