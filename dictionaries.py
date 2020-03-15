# !/usr/bin/python
# coding:utf-8

#dictionaries 是 json object 用 {} 表示
dict = {'k1':{'apple':3, 'orange': 5}, 'k2':['jay', 'thuy', 'ping'], 'k3':'v3'}

#列出 dictionaries 所有的 keys
print(dict.keys())

#列出 dictionaries 所有的 values
print(dict.values())

#列出 dictionaries 所有的物件
print(dict.items())

#訪問 dictionaries
print(dict['k1']['apple']) #3

print(dict['k2'][1]) #thuy

print(dict['k3']) #v3

# for loop in dictionaries
for k, v in dict.items():
	print('key:{} value:{}'.format(k, v))
