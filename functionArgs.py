# !/usr/bin/python
# coding:utf-8


def calToal(*args):
	'''
	* 的參數代表接收一個 tuple 參數物件
	'''
	for i in args:
		print(i)
	return sum(args)


result = calToal(1, 2, 3, 4, 5)
print(f'result:{result}')


def myFunc(**args):
	"""
	** 的參數代表接收一個 dictionaries 參數物件
	"""
	for k, v in args.items():
		print(f'key:{k} -> value:{v}')

myFunc(apple=20, orange=19, grape=17)