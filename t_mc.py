#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2014 yupeng <yupeng@yupengtekiMacBook-Air.local>
#
# Distributed under terms of the MIT license.

"""
mc_test
"""
import memcache

mc = memcache.Client(['127.0.0.1:11111'],debug=0)
mc.set('foo','bar')
val = mc.get('foo')
print val

dict1 = {'name':'yupeng','address':'hubei','sex':'female'}
mc.set('yupeng',dict1)
print mc.get('yupeng')

list1 = [{'name':'yupeng','address':'hubei'},{'name':'xxxx','address':'wuhan'}]

mc.set('t_list',list1)

print mc.get('t_list')
