# -*-coding:utf-8-*-
from quicksort import partition
import numpy as np
import random
"""
选取数组中的第i小的元素。如数组[1,2,3,4,5]中,3为第3小的元素
""""

def create_array(num):
    """
    产生[0,num)的随机数组随机数组
    """
    return random.sample(range(0, num), num)


def random_partition(arr, left, right):
    p = random.randint(left, right)
    arr[right], arr[p] = arr[p], arr[right]
    mid = partition(arr, left, right)
    return mid


def randomize_select(arr, left, right, i):
    if i < 0 or i + left - 1 > right:
        print('欲选取的元素超数组范围')
        return
    mid = random_partition(arr, left, right)
    if left == right:
        return [arr[left], left + 1]
    elif mid - left + 1 == i:
        return [arr[mid], mid + 1]
    elif mid - left + 1 > i:
        return randomize_select(arr, left, mid - 1, i)
    elif mid - left + 1 < i:
        return randomize_select(arr, mid + 1, right, i - mid - 1)


if __name__ == '__main__':
    """
    测试代码段1
    """
    a = create_array(20)
    print(a)
    result = randomize_select(a, 0, 19, 3)
    print(a)
    print(result)
    # """
    # 测试代码段2
    # """
    # a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    # random.shuffle(a)
    # print(a)
    # result = randomize_select(a, 0, 12, 3)
    # print(result)
