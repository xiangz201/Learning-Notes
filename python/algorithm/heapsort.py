# -*-coding:utf-8-*-
"""
堆排序
"""
import numpy as np


def create_array(num):
    return np.random.randint(20, size=num)


def max_heapify(arr, i):
    """
    维护堆
    """
    left = 2 * i + 1
    right = 2 * i + 2
    if left <= len(arr) - 1 and arr[i] < arr[left]:
        largest = left
    else:
        largest = i
    if right <= len(arr) - 1 and arr[largest] < arr[right]:
        largest = right
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        max_heapify(arr, largest)


def build_max_heap(arr):
    """
    建堆
    """
    for i in range((len(arr) - 2) // 2, -1, -1):
        max_heapify(arr, i)


def heap_sort(arr):
    """
    堆排序
    """
    build_max_heap(arr)
    last_num = len(arr) - 1
    ls = []
    for i in range(last_num, -1, -1):
        ls.append(arr[0])
        arr[0] = arr[i]
        arr = np.delete(arr, i, axis=0)
        last_num -= 1
        max_heapify(arr, 0)

    return ls


if __name__ == '__main__':
    arr1 = create_array(10)
    print(arr1)
    build_max_heap(arr1)
    print(arr1)
    arr2 = heap_sort(arr1)
    print(arr2)
