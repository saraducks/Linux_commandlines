import os,time

def call_func():
        x = 0
	for i in range(0,10):
	     x = x + 1

child_pid = os.fork()

if child_pid > 0:
	child = child_pid
        print("child process id", child)
else:
        print("Parent process id is",os.getppid())
	call_func()
        os._exit(0)

t = time.time()
print(t)
os.waitpid(child, 0)
print time.time() - t

