import numpy as np


def create_array(num):
    return np.random.randint(-10, 10, size=num)


def max_cross_subarray(low, mid, high, array):
    max_low, max_high = low, high
    left_sum = float("-inf")
    sum = 0
    for i in range(mid, low - 1, -1):
        sum += array[i]
        if sum > left_sum:
            left_sum = sum
            max_low = i
    right_sum = float("-inf")
    sum = 0
    for j in range(mid + 1, high + 1):
        sum += array[j]
        if sum > right_sum:
            right_sum = sum
            max_high = j
    max_sum = left_sum + right_sum
    return [max_low, max_high, max_sum]


def max_subarray(array, low, high):
    mid = (low + high) // 2
    if low == high:
        return [low, high, array[low]]
    else:
        l = max_subarray(array, low, mid)
        r = max_subarray(array, mid + 1, high)
        m = max_cross_subarray(low, mid, high, array)
        return max(l, r, m)


def max(a, b, c):
    if a[2] >= b[2] and a[2] >= c[2]:
        return a
    if b[2] >= a[2] and b[2] >= c[2]:
        return b
    else:
        return c


if __name__ == '__main__':
    arr = create_array(10)
    print(arr)
    result = max_subarray(arr,0,len(arr)-1)
    print(result)
