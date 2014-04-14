#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2014 yupeng <yupeng@yupengtekiMacBook-Air.local>
#
# Distributed under terms of the MIT license.

"""
test function param
"""

def test1(a,b):
    print a,b

test1(1,2)

def test2(a,b=2):
    print a,b

test2(1,2)
test2(1)

def test3(*a):
    print a

test3(1,2)
test3(1,2,3)

def test4(**a):
    print a

test4(x=1,y=2)

def test5(a,b,*args,**kwargs):
    print a,b,args,kwargs

test5(1,2,3,4,5,6,7,x=1,y=2,z=3)


