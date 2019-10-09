

def modifylist(lst):
    lst[0] += 10
    lst[-1] += 20

def test_modifylist():
    a = [ 1,3,70,15,25]
    print(a)
    modifylist(a)
    print(a)

####################################
    
def ReverseList(lst):
    pass     # implement the logic
    
   

def test_ReverseList():
    a = [ 1,3,70,15,25]
    print(a)
    ReverseList(a)
    print(a)    ###  expected [ 25, 15, 70, 3, 1]


#test_ReverseList()
    
###############################################    
    
def   testargs(x = 1, y = 'a'):
    print (x, '  ',  y)
    
def test_testargs():
        
    testargs()
    testargs(5)
    testargs(10,'c')
    testargs('E')
    testargs('X', 20)
    
    testargs(y = 100, x = 'abc')
    
    testargs(y = 100) # x takes 1, but y takes 100
    
    testargs(100)   # x takes 100


###############################################    
   
def add(*values): # variable no. of args are received as a tuple
        print(type(values), values)
        
        sum = 0
        for k in values:
                sum += k
        return sum
    
    
    
def test_add():
    print(add()) # tuple () is passed
    print(add(3,5,9,10)) # tuple (3,5,9,10) is passed
    
    
test_add()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    