#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2014 yupeng <yupeng@yupengtekiMacBook-Air.local>
#
# Distributed under terms of the MIT license.

"""
test false  {},[],(),0,'',None在python中都表示False
"""

if not {}:
    print 1

if not []:
    print 2

if not ():
    print 3

if not '':
    print 4

if not 0:
    print 5

if not None:
    print 6
