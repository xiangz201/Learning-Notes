# -*-coding:utf-8-*-
"""
二叉树的创建与遍历
以'#'表示子树终结
          1
      2        3
  4      #  #      6
#   #           7     #

其列表形式书写为[1, 2, 4, '#', '#', 5, '#', '#', 3, '#', 6, 7, '#', '#', '#']
=============================
isEmpty()                      判断是否为空,空则返回True，不空则返回False
build(list)                    生成二叉树的结构，返回根节点
build_tree(list)               生成二叉树，返回二叉树
preOrder_traversal()           先序遍历，返回遍历结果列表
inOrder_traversal()            中序遍历，返回遍历结果列表
inOrder_traversal()            后序遍历，返回遍历结果列表
bfs(node_root)                 广义优先遍历，返回遍历结果列表
dfs(node_root)                 未定义
=============================
example:
=============================
arr = [1, 2, 4, '#', '#', 5, '#', '#', 3, '#', 6, 7, '#', '#', '#']
tree = Tree()
print(tree.isEmpty())
my_tree = tree.build_tree(arr)
result_pre = my_tree.preOrder_traversal(my_tree.root)
result_in = my_tree.inOrder_traversal(my_tree.root)
result_post = my_tree.postOrder_traversal(my_tree.root)
result_bfs = my_tree.bfs(my_tree.root)
print('先序：', result_pre)
print('中序：', result_in)
print('后序：', result_post)
print('广义：', result_bfs)
============================
"""

from queue import Queue


class BTNode(object):
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


class Tree(object):
    # """
    # 迭代器方法
    # example
    # =============================
    # data_list = [1, 2, 4, '#', '#', 5, '#', '#', 3, '#', 6, 7, '#', '#', '#']
    # btree = Tree(data_list)
    # root = btree.createBiTree()
    # print(type(root))  #可以看出返回的是根节点Node节点
    # =============================
    # """
    # def __init__(self, data_list):
    #     # 初始化即将传入的列表的迭代器
    #     self.it = iter(data_list)
    #
    # def createBiTree(self, bt=None):
    #     try:
    #         # 步进获取下一个元素
    #         next_data = next(self.it)
    #         # 如果当前列表元素为'#', 则认为其为 None
    #         if next_data is "#":
    #             bt = None
    #         else:
    #             bt = BTNode(next_data)
    #             bt.left = self.createBiTree(bt.left)
    #             bt.right = self.createBiTree(bt.right)
    #     except Exception as e:
    #         print(e)
    #     return bt

    def __init__(self):
        self.root = None
        self.ls = [[] for _ in range(10)]

    def isEmpty(self):
        return self.root is None

    def build(self, list):
        key = list.pop(0)
        if key == '#':
            node = None
        else:
            node = BTNode(key)
            node.left = self.build(list)
            node.right = self.build(list)
        return node

    def build_tree(self, list):
        tree = Tree()
        tree.root = self.build(list)
        return tree

    def preOrder_traversal(self, node):
        if node is not None:
            self.ls[0].append(node.data)
            self.preOrder_traversal(node.left)
            self.preOrder_traversal(node.right)
        return self.ls[0]

    def inOrder_traversal(self, node):
        if node is not None:
            self.inOrder_traversal(node.left)
            self.ls[1].append(node.data)
            self.inOrder_traversal(node.right)

        return self.ls[1]

    def postOrder_traversal(self, node):
        if node is not None:
            self.postOrder_traversal(node.left)
            self.postOrder_traversal(node.right)
            self.ls[2].append(node.data)
        return self.ls[2]

    def bfs(self, node):
        """广义优先遍历就是从根节点出发，按层横向遍历。使用的是一个队列"""
        queue = Queue()
        if node is None:
            return
        else:
            queue.put(node)
            while not queue.empty() > 0:
                tree_node = queue.get()
                self.ls[3].append(tree_node.data)
                if tree_node.left is not None:
                    queue.put(tree_node.left)
                if tree_node.right is not None:
                    queue.put(tree_node.right)
        return self.ls[3]

    def dfs(self, node):
        """
        深度优先遍历是先序遍历的推广，从某个定点出发，一直遍历到最深处，然后回溯
        找到没有遍历到的点，再次应用深度优先遍历。使用的是一个栈。
        按我的理解树的深度优先遍历其实和先序遍历一样，
        也有大部分说法是先序中序后序都是树的深度优先遍历
        """
        pass


arr = [1, 2, 4, '#', '#', 5, '#', '#', 3, '#', 6, 7, '#', '#', '#']
tree = Tree()
print(tree.isEmpty())
my_tree = tree.build_tree(arr)
result_pre = my_tree.preOrder_traversal(my_tree.root)
result_in = my_tree.inOrder_traversal(my_tree.root)
result_post = my_tree.postOrder_traversal(my_tree.root)
result_bfs = my_tree.bfs(my_tree.root)
print('先序：', result_pre)
print('中序：', result_in)
print('后序：', result_post)
print('广义：', result_bfs)
