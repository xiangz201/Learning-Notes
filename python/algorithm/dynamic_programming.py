# -*-coding:utf-8-*-
"""
动态规划常用来求解最优化问题，一般按照如下4个步骤来设计动态规划算法
1、刻画一个最优解的结构特征
2、递归地定义最优解的值
3、计算最优解的值，通常采用自底向上的方法
4、利用计算得出的信息构建一个最优解
=============================
memoized_cut_rod(p: list, n: int)       自上向下算法
bottom_up_cut_rod(p: list, n: int)      自底向上的算法
extended_bottom_up_cut_rod(p,n)         保存最优切割点的钢条分割算法
print_cut_rod_solution(p, n)            打印切割点
print_matrix_chain_order(array_list, i,  j) 打印最有矩阵链乘法顺序
lcs_length(str_a: str, str_b: str)      打印最长子序列长度和序列，返回长度和最长子序列
space_efficient_lcs(str_a, str_b)       打印最长子序列长度
max_lcs(str_a, str_b)                   打印最长公共子字符串长度和序列，返回长度和序列
obst(p: list, q: list, n: int)          返回期望矩阵和切割点矩阵
=============================
example:
钢条切割
if __name__ == '__main__':
    p = [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
    print_cut_rod_solution(p,7)
    (r,s) = extended_bottom_up_cut_rod(p,10)
    print(r)
    print(s)
矩阵链乘法
import numpy as np
if __name__ == '__main__':
    array_list = [np.zeros((30, 35)), np.zeros((35, 15)), np.zeros((15, 5)), np.zeros((5, 10)),
                  np.zeros((10, 20)), np.zeros((20, 25))]
    print_matrix_chain_order(array_list, 1, 6)
最长公共子序列
if __name__ == '__main__':
    str_a = 'ABCBDABDHC'
    str_b = 'BDCABABH'
    (a,b)= lcs_length(str_a,str_b)
    print(a,b)
    space_efficient_lcs(str_a, str_b)
最优二叉搜索树
if __name__ == '__main__':
    p = [0, 0.15, 0.10, 0.05, 0.10, 0.20]
    q = [0.05, 0.10, 0.05, 0.05, 0.05, 0.10]
    (s, m) = obst(p, q, 5)
    print(s)
    print(m)
============================
"""

"""
钢条切割问题Page204
"""

'''带备忘录自顶向下'''


def memoized_cut_rod(p: list, n: int):
    r = [float('-inf')] * (n + 1)
    return memoized_cut_rod_aux(p, n, r)


def memoized_cut_rod_aux(p: list, n: int, r: list):
    if r[n] >= 0:
        return r[n]
    if n == 0:
        q = 0
    else:
        q = r[n]
        for i in range(1, n + 1):
            q = max(q, p[i] + memoized_cut_rod_aux(p, n - i, r))
    r[n] = q  # 记录段长为n的最大价格
    return q


'''自底向上'''


def bottom_up_cut_rod(p: list, n: int):
    r = [float('-inf')] * (n + 1)
    r[0] = 0
    for j in range(1, n + 1):  # 段长，从段长1开始计算知道段长为n
        q = float('-inf')
        for i in range(1, j + 1):
            q = max(q, p[i] + r[j - i])
        r[j] = q
    return r[n]


'''保存最优切割点'''


def extended_bottom_up_cut_rod(p: list, n: int):
    r = [float('-inf')] * (n + 1)
    s = [float('-inf')] * (n + 1)
    r[0] = 0
    s[0] = 0
    for j in range(1, n + 1):
        q = float('-inf')
        for i in range(1, j + 1):
            if q < p[i] + r[j - i]:
                q = p[i] + r[j - i]
                s[j] = i
        r[j] = q
    return r, s


def print_cut_rod_solution(p, n):
    (r, s) = extended_bottom_up_cut_rod(p, n)
    while n > 0:
        print(s[n])
        n = n - s[n]


"""
矩阵链乘法,数组p存储矩阵链的行和列
如A1×A2，那么A1的行和列为p0、p1，A2的行和列为p1、p2   
"""


def get_p(list):
    p = [0] * (len(list) + 2)
    m = 0
    n = 1
    for i in range(len(list)):
        (p[m], p[n]) = list[i].shape
        m += 1
        n += 1
    return p


def matrix_chain_order(ls):
    n = len(ls)
    p = [0] * (n + 1)
    p1 = 0
    p2 = 1
    for i in range(n):
        (p[p1], p[p2]) = ls[i].shape
        p1 += 1
        p2 += 1
    r = [[float('inf')] * (n + 1) for _ in range(n + 1)]  # r的横纵坐标代表链表段的首位
    s = [[float('inf')] * (n + 1) for _ in range(n + 1)]  # s记录切割点
    r[0][0] = s[0][0] = 0
    for i in range(1, n + 1):  # 收尾相同段长为1，记为0
        r[i][i] = 0
    for le in range(2, n + 1):  # len表示段长，从段长为2到段长为n
        for i in range(1, n - le + 2):  # i表示起始元素
            for k in range(i, i + le - 1):  # k表示切割点，把链表分为Ai—Ak，A(k+1)—A(i+len-1)两段
                q = r[i][k] + r[k + 1][i + le - 1] + p[i - 1] * p[k] * p[i + le - 1]
                if q < r[i][i + le - 1]:
                    r[i][i + le - 1] = q
                    s[i][i + le - 1] = k
    return r, s


def print_optimal_parens(s: list, i: int, j: int):
    if i == j:
        print('A%d' % i, end='')
    else:
        print('(', end='')
        print_optimal_parens(s, i, s[i][j])
        print_optimal_parens(s, s[i][j] + 1, j)
        print(')', end='')


def print_matrix_chain_order(array_list: list, i: int, j: int):
    (r, s) = matrix_chain_order(array_list)
    print_optimal_parens(s, i, j)


"""
最长公共子序列
"""


def lcs_length(str_a: str, str_b: str):
    if len(str_a) == 0 or len(str_b) == 0:
        return 0
    # dp = [[0]*len(str_b) for _ in range(len(str_a)]
    dp = [[0 for _ in range(len(str_b) + 1)] for _ in range(len(str_a) + 1)]
    for i in range(1, len(str_a) + 1):
        for j in range(1, len(str_b) + 1):
            if str_a[i - 1] == str_b[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    i, j = len(str_a), len(str_b)
    LCS = ''
    while i > 0 and j > 0:
        if str_a[i - 1] == str_b[j - 1] and dp[i][j] == dp[i - 1][j - 1] + 1:
            LCS = str_a[i - 1] + LCS
            i, j = i - 1, j - 1
            continue
        if dp[i][j] == dp[i - 1][j]:
            i, j = i - 1, j
            continue
        if dp[i][j] == dp[i][j - 1]:
            i, j = i, j - 1
            continue
    print('The length of LCS is %d\nLCS is %s' % (dp[len(str_a)][len(str_b)], LCS))
    return dp[len(str_a)][len(str_b)], LCS


def space_efficient_lcs(str_a, str_b):
    """
    降低空间复杂度的动态规划算法
    """
    if len(str_a) == 0 or len(str_b) == 0:
        return 0
    dp = [0 for _ in range(len(str_b) + 1)]
    for i in range(1, len(str_a) + 1):
        left_up = 0
        dp[0] = 0
        for j in range(1, len(str_b) + 1):
            left = dp[j - 1]
            up = dp[j]
            if str_a[i - 1] == str_b[j - 1]:
                dp[j] = left_up + 1
            else:
                dp[j] = max([left, up])
            left_up = up
    print(dp[len(str_b)])


"""
最长公共子字符串
"""


def max_lcs(str_a, str_b):
    if len(str_a) == 0 or len(str_b) == 0:
        return None
    max_len = 0
    max_lcs = ''
    dp = [[0 for _ in range(len(str_b) + 1)] for _ in range(len(str_a) + 1)]
    for i in range(1, len(str_a) + 1):
        for j in range(1, len(str_b) + 1):
            if str_a[i - 1] == str_b[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                max_len = max(max_len, dp[i][j])
                if max_len == dp[i][j]:
                    max_lcs = str_a[i - max_len:i]
            else:
                dp[i][j] = 0
    print('The length of LCS is %d\nLCS is:%s' % (max_len, max_lcs))
    return max_len, max_lcs


"""
最优二叉搜索树
"""


def obst(p: list, q: list, n: int):  # p为非叶节点的概率，q为叶节点的概率。叶节点表示未找到
    e = [[float('inf') for _ in range(n + 1)] for _ in range(n + 2)]  # 存储每种节点段的期望
    w = [[float('inf') for _ in range(n + 1)] for _ in range(n + 2)]  # 存储增加一个节点带来的期望代价
    root = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
    for i in range(1, n + 2):
        e[i][i - 1] = q[i - 1]
        w[i][i - 1] = q[i - 1]
    for l in range(1, n + 1):
        for i in range(1, n - l + 2):
            end = i + l - 1
            # e[i][end] = float('inf')
            w[i][end] = w[i][end - 1] + q[end] + p[end]  # 增加的代价为所有节点深度加1，即把所有节点都加一遍
            for k in range(i, end + 1):
                t = e[i][k - 1] + e[k + 1][end] + w[i][end]
                if t < e[i][end]:
                    e[i][end] = t
                    root[i][end] = k
    return e, root
