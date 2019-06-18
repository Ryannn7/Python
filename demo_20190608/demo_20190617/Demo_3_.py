#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#@Author:liuzongshuai
#@Time:2019/6/8
#@Name:Demo_3_

#本篇开始讲述Python的高级特性：
# L=[]
# n=1
# while n<99:
#     L.append(n)
#     n+2

#第一节：切片
L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
r=[]
n=3
for i in range(n):
    r.append(L[i])
#print(r)
#The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and ends at a specified number.
#range(start, stop, step)
# start	Optional. An integer number specifying at which position to start. Default is 0
# stop	Optional. An integer number specifying at which position to end.
# step	Optional. An integer number specifying the incrementation. Default is 1

# print(L[0:5])
# print(L[:3])
# print(L[1:3])
# print(L[-1:])
# print(L[-3:])

L=list( range(100))
L[:10]
L[-10:]
L[:10:2]
L[::5]
#print(L)
T=(0, 1, 2, 3, 4, 5)
print(T[:3])
print('ABCDEFG'[:3])