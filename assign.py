# -*- coding: utf-8 -*-
"""
Created on Sun Aug 15 18:31:18 2021

@author: suba
"""
list=["suba","bala","kalai","hema","abi"]

list.append("sanjay")
print(list)

list.remove("abi")
print(list)

list.copy()
print(list)

x=list.count("suba")
print(x)

list1=["dhana","sasi"]
list.extend(list1)
print(list)

x=list.index("sanjay")
print(x)

list.insert(1,"nivetha")
print(list)

list.pop(6)
print(list)

list.reverse()
print(list)

list.sort()
print(list)

list.clear()
print(list)