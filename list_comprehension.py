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
# Exercise: the result should contain the characters of the string variable using list comprehesnion
string = "Hello, world!"
chars = [ch for ch in string]
print(chars)

# ---------------------------------- Day 5 ----------------------------------
# Exercise: the result should contains the keys of the given dictionary
dictionary = {"one": 1, "two": 2, "three": 3}
dict_keys = [key for key in dictionary.keys()]
print(dict_keys)

# ---------------------------------- Day 6 ----------------------------------
# Doing above all these exercise using list()
print(list(range(10)))
print(list(string))
print(list(dictionary))

# ---------------------------------- Day 8 ----------------------------------
# Exercise: rewriting given code below as list comprehension
# values = []
# for num in range(10, 23, 2):
#     values.append(num % 13)
values = [num % 13 for num in range(10, 23, 2)]
print(values)

# ---------------------------------- Day 9 ----------------------------------
# Exercise: rewriting the loop below as a list comprehension
# string = "I like pizza"
# doubled = []
# for char in string:
#     doubled.append(2 * char)
string1 = "I like pizza"
doubled = [2 * char for char in string1]
print(doubled)

# ---------------------------------- Day 10 ----------------------------------
# Exercise: rewriting the loop below as a list comprehension
# firsts = []
# for word in "The quick brown fox jumps.".split():
#     firsts.append(word[0])
firsts = [word[0] for word in "The quick brown fox jumps.".split()]
print(firsts)

# ---------------------------------- Day 11 ----------------------------------
# Exercise: rewriting the loop below as a list comprehension
numbers = [42, 73, 0, 16, 10]
is_big = [num > 10 for num in numbers]
print(is_big)
