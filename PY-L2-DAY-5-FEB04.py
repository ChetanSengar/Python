import threading

bal = 1000

def   getThreadName():
   return( threading.currentThread().getName() )


def counterop(lock, vals):
   global bal
   for _ in range(1000):
      for k in range(0,len(vals)):
          print(getThreadName(),'acquiring lock')
          #lock.acquire() 
          print(getThreadName(),'acquired lock')
          bal += vals[k]
          lock.release()
          print(getThreadName(),'released lock')

def mt_lock_demo():
   global bal

   vals1 = [25, 30, 15, 25, 35, 11 ]
   vals2 = [-15, -10, -25, -15, -5, -21 ]

   lock = threading.Lock()    # create mutex lock
   t1 = threading.Thread(target=counterop, args=(lock, vals1))
   t1.start()

   t2 = threading.Thread(target=counterop, args=(lock, vals2))
   t2.start()

   t1.join()
   t2.join()
   print('bal = ', bal)


#mt_lock_demo()
   
   
import re   
######################
   
   
def regex1():
    text="one.two:three,four"
    r = re.search("\w+:", text)
    print(r)
    if r == None:
        print('pat not found')
    else:
        print('pat is - ', r.group())
   

def regex2():
    text="one,two,123,three,four,345"
    r = re.search("\d+,", text)
    print(r)
    if r == None:
        print('pat not found')
    else:
        print('pat is - ', r.group())
   
       
def regex3():
    strings = ["123,456,789,,,,,",  "123,456,,789,,","123", ""] 

    for s in strings:
      matches=re.finditer(",", s)
      print(matches)
      n=0
      for k in matches:
         n += 1
      print (n)


def regex_sub():
    s = "jan feb mar apr"
    ns = re.sub('r','R', s) ## all rs are replaced
    print(s)
    print(ns)
   
    ns = re.sub('a','A', s) ## all as are replaced
    print(s)
    print(ns)

    ns = re.sub('a','A', s, 2) ## ????
    print(s)
    print(ns)


def regex_4():
    strs = [ 'abc', 'abcab', 'abcAb', 'abABx', 'xABxxab' ]
    for s in strs:
      print (s)
      findObj=re.match('(.+)(.+)(.*)\\1\\2',s, re.IGNORECASE)
      if not findObj == None:
            print ('  ', s, ':', findObj.group(1)+'  '+findObj.group(2)+'   '+findObj.group(3))
    


class Cube:
    def __init__(self,maxx):
        self.maxx=maxx
        self.n = 1
    def __iter__(self):
        #self.n=1
        return self
    def __next__(self):
        if self.n<=self.maxx:
            result = self.n**3
            self.n+=1
            return result
        else:
            raise StopIteration




def testCube():
    for k in Cube(5):
        print(k)

testCube()














