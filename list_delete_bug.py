x = [0, 1, 2, 3, 4, 5, 6, 7]


def incorrect_delete_func(del_list):
    """
    如果需要使用索引來刪除 list 內的元素，
    例如刪除索引位置:1、3、5...的元素，
    下方程式邏輯是對的，但結果卻是錯的，
    這是因為刪除元素時，後面的元素的索引編
    號會立即往前遞補，這樣整個 list 的索引
    都已經改變，自然導致透過索引刪除元素都是錯的。
    """
    for i, num in enumerate(x):
        if i % 2 == 1:
            del x[i]

    print(x)


def correct_delete_func(del_list):
    """
    正確刪除的方式須由 list 的後面往前刪除
    """
    # 使用range()產生由 list 後面往前的 index: 7,6,5,4,3,2,1
    index_list = range(len(x) - 1, -1, -1)

    for i in index_list:
        if i % 2 == 1:
            del x[i]


"""
更簡潔、易讀的方式就是使用 comprehension(生成式)
"""
x = [n for i, n in enumerate(x) if not i % 2 == 1]
print(x)