
"""
    test list or set
"""
#!/usr/bin/env python
# encoding: utf-8

from time import time
t = time()
lista=[1,2,3,4,5,6,7,8,9,13,34,53,42,44]
listb=[2,4,6,9,23]
intersection=[]
for i in range (1000000):
    for a in lista:
        for b in listb:
            if a == b:
                intersection.append(a)
print "total run time:"
print time()-t
from time import time
t = time()
lista=[1,2,3,4,5,6,7,8,9,13,34,53,42,44]
listb=[2,4,6,9,23]
intersection=[]
for i in range (1000000):
    list(set(lista)&set(listb))
print "total run time:"
print time()-t

