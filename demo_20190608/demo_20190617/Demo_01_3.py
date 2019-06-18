#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#@Author:liuzongshuai
#@Time:2019/6/8
#@Name:Demo_03

# print('Age : %d,Gender: %s' %(25.0,True))
# print('Hello ,{0},成绩提升了：{1}%'.format('小明',15))

# a=0
# if(a>=18):
#     print('your age is:',a)
# elif (a<=17 and a>=5):
#     print('Haahaha young boy')
# elif (a>=1):
#     print("1111111111")
# else   :
#     print("=============")

#
# age=input('birth:')
# ageNum=int(age)
# if(ageNum>18):
#     print('adult')
# else:
#     print('Boy')

#print('==============第三节：循环===============')
# list=['Lily','Ryan','Tony']
# for name in list:
#     print(name)
# sum=0
# for num in range(101):
#     sum=sum+num
# print('sum=',sum)
#
#
# sum=0
# n=0
# while n<100:
#     n = n + 1
#     sum = sum + n
#     if(n%2==1):
#         break
#     print(n)
# print('sum=',sum)
print('==============第四节：dict & set===============')
demoDic={'Macky':45,'Lucy':89,'Sydia':90}
print(demoDic['Macky'])

demoDic['Macky']=87
print(demoDic['Macky'])
print(demoDic.get('Ryan',100))

print('niu' in demoDic)
s=set([1,2,3])
print(s)

s=set(['a','b',('m','n')])
s.add('hello')
s.remove('a')
s.set(['1',2])
print(s)




