"""
test

"""
#!/usr/bin/env python
# encoding: utf-8



from time import time
t = time()
s = ""
list = ['a','b','b','d','e','f','g','h','i','j','k','l','m','n']
for i in range (10000):
    for substr in list:
        s+= substr
print "total run time:"
print time()-t
