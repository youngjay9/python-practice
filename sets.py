# !/usr/bin/python
# coding:utf-8

# 將 mySet 初始化一個 set 物件
mySet = set()

mySet.add(1)
print(mySet) #1

mySet.add(1)
print(mySet) #1

mySet.add(2)
print(mySet) #1,2

# 過濾 list 中重複的元素
myList = [1,2,2,3,4,5,5]

setList = set(myList)
print(setList) # [1, 2, 3, 4, 5]

print(set([1,1,2,3]))
