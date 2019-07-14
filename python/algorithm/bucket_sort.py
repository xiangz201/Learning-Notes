# -*- coding:utf-8 -*-
""""
桶排序
"""
import numpy as np


def create_array(num):
    return np.random.randint(50, size=num)


def bucket_sort(arr):
    max_elm = np.max(arr)
    string = str(max_elm)
    lenght = len(string)

    for i in range(lenght):
        b = [[] for _ in range(10)]
        for elem in arr:
            if len(str(elem)) - 1 < i: #如何数字小于符合这一轮桶的排序的范围
                b[0].append(elem)
            else:
                # 取整数的各个位数
                list_elem = list(str(elem))
                list_elem.reverse()
                flag = list_elem[i]
                # 按位数加入桶中
                b[int(flag)].append(elem)
        ls = []
        for x in b:
            ls.extend(x)
        arr = ls
    return arr


if __name__ == '__main__':
    a = create_array(10)
    print(a)
    a = bucket_sort(a)
    print(a)
