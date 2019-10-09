import math

class Circle:
    def __init__(self, r):
        self.__r = r
        
    def area(self):
        return  math.pi * self.__r ** 2
    
    @property
    def perimeter(self):
        return 2 * math.pi * self.__r
    
    def setradius(self, r):
        self.__r = r

   
    @property
    def r(self):
        return self.__r
     
 
    @r.setter
    def r(self,r):
        self.__r = r
 
    
    def getradius(self) :
        return self.__r
    
    
def test_circle():
    c = Circle(5.0)
    #print(c.__r)
    print('area = ', c.area())
    print('perimeter = ', c.perimeter)
    
    c.__r = 30   # did not modify, but no error reported
    #c.setradius(10)
    c.r = 10
    print('area = ', c.area())
    print('perimeter = ', c.perimeter)    
    
    print('radius - ', c.getradius())
    
    print('----------')
    c2 = Circle(25.0)
    print('area = ', c2.area())
    print('perimeter = ', c2.perimeter)    
    c2.r = 30
    print('area = ', c2.area())
    print('perimeter = ', c2.perimeter)    
    
    
    
    
#test_circle()
    
    
    
    
    
    

"""   
#######  CRC Cards
###############  Class Responsibility  Collaboration    
"""

 
class ShoppingItem:
    def __init__(self,code,price):
        self.code = code
        self.price = price
    
    
class Book(ShoppingItem):
    def __init__(self, code,auth,title,isbn, price):
        super().__init__(code,price)
        self.auth = auth
        self.title = title
        self.isbn = isbn
        
    def showSamplePages(self):
        print("Book::samplepages() - TBD")
        
    def __str__(self):
        return    "[{}] {} Rs.{}".format(self.code, self.title, self.price)
            
        
    
class EBook(Book):
    def __init__(self, code,title, auth,isbn, price, fmt, size):
        super().__init__(code,auth,title,isbn, price)
        self.format = fmt;  ## PDF etc
        self.filesize = size   # KB
        
    def showSamplePages(self):
        print("EBook::samplepages() - TBD")
        
    def playBook(self):
        print("EBook::playBook() - TBD")
        
    def __str__(self):
        return "{}-{}-{}-{}KB".format(self.code,self.auth,self.price, self.filesize)
  
    
def test_shopping ():
    ebk1 = EBook(1001, "Prog in Py", "Tim", 12345, 390, "PDF", 2300 )
    ebk1.playBook()
    print(ebk1)
    
    bk = Book(2001, "Advance Py", "cook", 30568, 790)
    bk.showSamplePages()
    print(bk)
    
    
    items = [ebk1, bk]
    
    print('----------')
    for k in items:
        print(k)
        """
        # if ebook, then play        
        # if book,  show sample page
        """
        if isinstance(k, EBook):
            k.playBook()
            
        if isinstance(k, Book):
            k.showSamplePages()
            
    
    
    
test_shopping()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    