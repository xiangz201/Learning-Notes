# -*-coding:utf-8-*-
"""
快速排序
"""
import numpy as np


def create_array(num):
    return np.random.randint(20, size=num)


def partition(arr, left, right):
    pivot = arr[right]
    i = left - 1
    for j in range(left, right):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[right] = arr[right], arr[i + 1]
    return i + 1


def quick_sort(arr, left, right):
    if left <= right:
        mid = partition(arr, left, right)
        quick_sort(arr, left, mid - 1)
        quick_sort(arr, mid + 1, right)


if __name__ == '__main__':
    arr1 = create_array(10)
    print(arr1)
    quick_sort(arr1, 0, len(arr1) - 1)
    print(arr1)
