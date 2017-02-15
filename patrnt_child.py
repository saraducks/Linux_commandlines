import os

print os.getppid()              
print os.getpid()               
def demo():                     
   print os.getpid()
   if 5 > 0:
 	print("inside child process ",os.getpid())

demo()
print os.getpid()

