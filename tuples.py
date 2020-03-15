# !/usr/bin/python
# coding:utf-8

#tuples 用 () 表式, 資料結構跟 list 一樣, 但它的項目為 immutability, 既有的項目無法變更,也無法 append 新的項目
t = ('a', {'k1':'v1'}, [0,1,2])

#list 用 [] 表式, 它的項目為 mutability, 既有的項目可以變更,也可 append 新的項目
list = ['a', {'k1':'v1'}, [0,1,2]]

#<type 'tuple'>
print('type(t):{}', type(t))

#<type 'list'>
print('type(list):{}', type(list))

#計算 a 元素的個數
print('t,count(a):{}',t.count('a')) #1 

#list 既有的項目可以變更
list[0] = 'New Item'
print('list:{}', list)

#tuples 既有的項目無法變更 ==> TypeError: 'tuple' object does not support item assignment
# t[0] = 'New Item'

# 訪問 tuples 
print(t[0]) #a

print(t[1]['k1']) #v1

print(t[2][2]) #2






