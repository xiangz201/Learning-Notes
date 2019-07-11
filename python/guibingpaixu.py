# -*-coding:utf-8-*-
"""
归并排序算法
"""

import numpy as np


def create_array(a):
    """产生随机数组"""
    return np.random.randint(0, 10, size=10)


"""方法1：对数组整体排序 """


def merge1(list1, list2):
    ls = []
    i = j = 0
    while i < len(list1) and j < len(list2):
        if list1[i] > list2[j]:
            ls.append(list2[j])
            j += 1
        else:
            ls.append(list1[i])
            i += 1

    if i < len(list1):
        ls.extend(list1[i:len(list1)])
    if j < len(list2):
        ls.extend(list2[j:len(list2)])

    return ls


def merge_sort1(lists):
    if len(lists) <= 1:
        return lists
    middle = (len(lists)) // 2
    left = merge_sort1(lists[0:middle])
    right = merge_sort1(lists[middle:])
    return merge1(left, right)


"""方法2：对数组部分排序 """


def merge2(a, left, middle, right):
    l1 = [0] * (middle - left + 1)
    r1 = [0] * (right - middle)

    for i in range(0, middle - left + 1):
        l1[i] = a[left + i]

    for j in range(0, right - middle):
        r1[j] = a[middle + 1 + j]
    i = j = 0
    k = left
    while i < len(l1) and j < len(r1):
        if l1[i] < r1[j]:
            a[k] = l1[i]
            i += 1
        else:
            a[k] = r1[j]
            j += 1
        k += 1
    while i < len(l1):
        a[k] = l1[i]
        k += 1
        i += 1
    while j < len(r1):
        a[k] = r1[j]
        k += 1
        j += 1


def merge_sort2(a, left, right):
    if left < right:
        s = int((right + left) / 2)
        merge_sort2(a, left, s)
        merge_sort2(a, s + 1, right)
        merge2(a, left, s, right)


if __name__ == '__main__':
    arr1 = create_array(10)
    print('元素组:', arr1)
    merge_sort1(arr1)
    print('排序后:', arr1)
    arr2 = create_array(10)
    print('元素组:', arr2)
    merge_sort2(arr2, 0, 9)
    print('排序后:', arr2)
