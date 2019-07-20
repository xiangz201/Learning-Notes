# -*-coding:utf-8-*-
"""
图的广义优先遍历（bfs）和深度优先遍历（dfs）
广义优先遍历就是从根节点出发，按层横向遍历。使用的是一个队列.
深度优先遍历是先序遍历的推广，从某个定点出发，一直遍历到最深处，然后回溯找到没有遍历到的点，再次应用深度优先遍历。使用的是一个栈。
=============================
bfs(node_root)                   广义优先遍历，返回遍历结果列表
dfs(node_root)                   深度优先遍历，非递归方法，返回遍历结果列表
dfs_iter(G, cur, label = set())  深度优先遍历，递归方法，返回遍历结果列表
=============================
"""
from queue import Queue


class node(object):
    def __init__(self, data=None, next=None):
        self.next = next
        self.data = data


def bfs(node):
    result = []
    if node is None:
        return
    queue = Queue()
    label = set()
    queue.put(node)
    label.add(node)
    while not queue.empty():
        cur = queue.get()
        result.append(cur.value)
        for next in cur.next:
            if next not in label:
                queue.put(next)
                label.add(next)
    return result


def dfs(node):
    result = []
    if node is None:
        return
    label = set()
    stack = []
    label.add(node)
    stack.append(node)
    while len(stack)>0:
        cur = stack.pop()
        if cur not in label:
            label.add(cur)
            result.append(cur.value)
        for next in cur.next:
            if next not in label:
                stack.append(next)
    return result


def dfs_inter(G, cur, label=set()):
    print(cur.value)
    label.add(cur)
    #G(cur)表示cur的相邻顶点    
    for u in G(cur):
        if u not in label:
            dfs(G,u,label)
        

