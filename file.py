# !/usr/bin/python
# coding:utf-8

# 在 python3 可以用 with ... as...語法來簡化 try... except ... finally 語句
# with 語句會自動執行 file.close()
# 即使在with as的區塊中發生了例外，最後一定會關閉file所參考的物件

#讀取檔案(每次讀一行)
with open('myFile.txt', mode='r') as file:
	for line in file:
		print(line)

#寫入檔案，使用 append 的方式
list = ['one', 'two', 'three']
with open('myNewFile.txt', mode='a') as file:
	for line in list:
		file.write(line + '\n')

#寫入檔案，使用覆寫的方式
list2 = ['over', 'writting']
with open('myNewFile.txt', mode='w') as file:
	for line in list2:
		file.write(line)	