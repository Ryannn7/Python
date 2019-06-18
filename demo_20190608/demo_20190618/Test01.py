#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#@Author:liuzongshuai
#@Time:2019/6/18
#@Name:Test01

def power(x):
    return  x*x
a=power(5)
# print(a)

def power(x,n):
    s=1
    while n>0:
        n=n-1
        s=s*x
    return s
#print(power(5,5))

#默认参数：
def enroll(name, gender, age=6, city='Beijing'):
    print('name:', name)
    print('gender:', gender)
    print('age:', age)
    print('city:', city)
#a=enroll('张明','男')

def add_end(L=None):
    if L is None:
        L=[]
    L.append('END')
    return L
#print(add_end())

#可变参数：
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum
#print(calc(2,3,4,5))


#可变参数:对于


