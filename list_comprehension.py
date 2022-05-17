#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# Created By  : wasif
# Created Date: 17/05/2022
# version ='1.0'
# ---------------------------------------------------------------------------
""" This is 100 day challenge of learning python list comprehension by twitter (@mathsppblog) """ 
# ---------------------------------------------------------------------------
# ---------------------------------- Day 1 ----------------------------------
# list comprehension syntax
# [func(elem) for elem in iterable if cond(elem)]

# ---------------------------------- Day 2 ----------------------------------
numbers = []
for i in range(10):
    numbers.append(1 + i ** 2)

print("Vanilla Numbers:", numbers)

numbers = [1 + i ** 2 for i in range(10)]
print("List compr. Numbers:", numbers)

# ---------------------------------- Day 3 ----------------------------------
# Exercise: list contains integer from 0 to 9 using list comprehesnion
int_list = [i for i in range(10)]
print(int_list)

# ---------------------------------- Day 4 ----------------------------------
# Exercise: list contains integer from 0 to 9 using list comprehesnion
string = "Hello, world!"
chars = [ch for ch in string]
print(chars)