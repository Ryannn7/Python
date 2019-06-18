#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#@Author:liuzongshuai
#@Time:2019/6/8
#@Name:Demo_2_01

#
# def my_abs(x):
#     if not isinstance(x,(int,float)):
#         raise TypeError('bad Operand Type')
#     if(x>=9):
#         return x
#     if(x>0):
#         return -x
#     else :
#         return None
#
# def pop():
#     pass


#定义函数:返回多个值：
# import math
# def move(x,y,step,angle=0):
#     nx=x+step*math.cos(angle)
#     ny=y-step*math.sin(angle)
#     return nx,ny
#
#
#
# a=move(100,100,60,math.pi/6)
# print(a)
#
# my_abs(-8)


# print('=========作业=======')
# import math
# def quadratic(a, b, c):
#    n=math.sqrt(b*b-4*a*c)
#    n1=(-b+n)/2*a
#    n2=(-b-n)/2*a
#    return n1,n2
#
# print( quadratic(2,3,1))


#print('=========函数的参数：=======')
def power(x, n):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s

#print(power(5,3))


def power(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s
#print(power(5))


#print('=========函数可变参数：=======')
def add_end(L=[]):
    L.append('END')
    return L

def add_endPro(L=None):
    if(L is None):
        L=[]
    L.append('END')
    return L

#print( add_end())
#print( add_endPro())



# def add_end2(L=[]):
#     L.append('END')
#     return L
# print(add_end2())
# print(add_end2(['1','m','n']))


#print('=========关键字参数：=======')
def cal(number):
    sum=0
    for num in number:
        sum=sum+num
    return sum

lisStr=[1,2,3,4,5,6,7,8,9,10]
#print( cal(lisStr))
def cal(*number):
    sum=0
    for num in number:
        sum=sum+num
    return sum

#print(cal(1,2,3,4,5))
#print(cal(*lisStr))

#print('=============关键字参数：===========')
def person(name,age,**kw):
    print('name:',name,'age',age,'other',kw)
# person('John',30,city='Beijing')
# extra={'city':'Beijing','job':'Engineer'}
# #在接收dic类型的数据的部分或者全部值的时候可以用**dic
# person('Mackle',40,**extra)
# #关键字参数可以接收任务多个dict类型的数据
# person('Mackle',40,gender='m',job='Engineer')


#print('========命名关键字参数================')
#使用命名关键字参数时，要特别注意，如果没有可变参数，就必须加一个*作为特殊分隔符。如果缺少*，Python解释器将无法识别位置参数和命名关键字参数：
def person(name, age, city, job):
    # 缺少 *，city和job被视为位置参数
    pass

def defin(name,age,*,city ,job):
    print('name:',name,'job:',job,'city:',city,'job:',job)
#defin('王强',29,'beijing','Enginer')
#defin('王强',29,city='beijing',job='Enginer')

#参数组合
#在Python中定义函数，可以用必选参数、默认参数、可变参数、关键字参数和命名关键字参数，这5种参数都可以组合使用。但是请注意，参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。
#比如定义一个函数，包含上述若干种参数：
def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)

def f2(a, b, c=0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)

args = (1, 2, 3)
kw = {'d': 88, 'x': '#'}
#f2(*args, **kw)


print('=============递归函数============')
def func(n):
    if (n==1):
        return 1
    return n*func(n-1)
print( func(100))



#尾递归优化：尾递归是指，在函数返回的时候，调用自身本身，并且，return语句不能包含表达式。这样，编译器或者解释器就可以把尾递归做优化，使递归本身无论调用多少次，都只占用一个栈帧，不会出现栈溢出的情况。
#遗憾的是：遗憾的是，大多数编程语言没有针对尾递归做优化，Python解释器也没有做优化，所以，即使把上面的fact(n)函数改成尾递归方式，也会导致栈溢出。
def fact(n):
    return fact_iter(n, 1)

def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)
print(fact(100))













