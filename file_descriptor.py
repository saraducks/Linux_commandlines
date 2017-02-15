import sys
import resource

file1 = open('/Users/sara/my_code/linux_commands_practise/commands.txt')
print(file1.fileno())
file2 = open('/etc/hosts')
print(file2.fileno())
file3 = open('/etc/passwd')
print(file3.fileno())
file1.close()
file2.close()
file3.close()

file4= open('/dev/null')
print(file4.fileno())
file4.close()

print(sys.stdin.fileno())
print(sys.stdout.fileno())
print(sys.stderr.fileno())

l = resource.getrlimit(3)
print(l)

