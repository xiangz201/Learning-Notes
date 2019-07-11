# -*-coding:utf-8-*-
import numpy as np


def creat_array(num):
    return np.random.randint(num, size=num)


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


if __name__ == '__main__':
    a = creat_array(10)
    print(a)
    insertion_sort(a)
    print(a)
