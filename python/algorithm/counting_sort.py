# -*-coding:utf-8-*-
"""
计数排序
"""
import numpy as np


def create_array(num):
    return np.random.randint(20, size=num)


def counting_sort(arr1):
    k = np.max(arr1)  # k为arr1中最大的数
    c = np.zeros(k + 1, int)  # 建立一个数组，记录位置等于arr1中元素的个数
    arr2 = np.zeros(len(arr1), int)
    for i in arr1:
        c[i] = c[i] + 1
    for i in range(1, k + 1):
        c[i] = c[i] + c[i - 1]
    for j in range(len(arr1) - 1, -1, -1):
        arr2[c[arr1[j]] - 1] = arr1[j]
        c[arr1[j]] = c[arr1[j]] - 1
    return arr2


if __name__ == '__main__':
    a1 = create_array(5)
    print(a1)
    a2 = counting_sort(a1)
    print(a2)
