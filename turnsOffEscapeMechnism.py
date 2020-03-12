# windows 的路徑字串會造成跳脫字元，在字串前面加一個 r 會關閉跳脫字元的機制
path = r"C:\new\text.dat"

print(path)