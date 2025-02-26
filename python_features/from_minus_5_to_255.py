import sys
a = 256
b = 256
print(a is b)
print(sys.getrefcount(a))

a = 13333000
b = 13333000
print(a is b)
print(sys.getrefcount(a))

