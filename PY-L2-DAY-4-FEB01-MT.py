import threading, time      
"""
# threading module is needed for multithread app 			
# that uses high-level threading model 
"""


def  threadfn1():
    print('in thread function')


def thread_demo1():
    t1 = threading.Thread(target=threadfn1)   # create & configure thread
    t1.start()   # let the thread run


#######################
    
def   getThreadName():
   return( threading.currentThread().getName() )

def   threadfn2(n):
   print(getThreadName(), ": started")
   print(getThreadName(), ": thread sleeps for", n, "sec")
   for k in range(1,8):
         print(getThreadName(), k)
         #time.sleep(n)
   print(getThreadName(), ": terminating")

def thread_demo2():
    t1 = threading.Thread(name="T1", target=threadfn2, args=(1,))
    t1.start()  # not a blocking call
    t2 = threading.Thread(name="T2", target=threadfn2, args=(3,))
    t2.start()


thread_demo2()

