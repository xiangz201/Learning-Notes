# -*-coding:utf-8-*-
"""
二叉搜索树的插入，删除，查询操作
=============================
search(val)                    判断是否存在值val,存在则返回True，不空则返回False
insert(root,val)               在以root为根节点的二叉搜索树中插入值val,返回根节点
find_min(root)                 返回以root为根节点的二叉树的最小值所在的节点
find_max(root)                 返回以root为根节点的二叉树的最大值所在的节点
find_parent(node):             返回node节点双亲节点，没有则返回None
find_successor(root)           返回root节点的后继节点，没有则返回None
delete_node(root,val)          删除以root为根节点的二叉搜索树的值为val的节点，返回根节点
=============================
example:构建如下搜索树
           12
    5               18
2       9      15          19
                   17
=============================
tree = bsf(TreeNode(12))
tree.insert(tree.root, 5)
tree.insert(tree.root, 2)
tree.insert(tree.root, 9)
tree.insert(tree.root, 18)
tree.insert(tree.root, 15)
tree.insert(tree.root, 19)
tree.insert(tree.root, 17)
result = tree.delete_node(tree.root,12)
print(result.val)    #结果是15
============================
"""


class TreeNode(object):
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        self.ls = [[] for _ in range(10)]


class bsf(object):
    def __init__(self, node=None):
        self.root = node

    def search(self, key):
        if self.root is None:
            return False
        else:
            node = self.root
            while node:
                if node.val == key:
                    return True
                elif node.val > key:
                    node = node.left
                elif node.val < key:
                    node = node.right
            return False

    def insert(self, root, val):
        if root is None:
            root = TreeNode(val)
        elif val < root.val:
            root.left = self.insert(root.left, val)
        elif val > root.val:
            root.right = self.insert(root.right, val)
        return root

    def find_min(self, root):
        if root.left:
            return self.find_min(root.left)
        else:
            return root

    def find_max(self, root):
        if root.right:
            return self.find_max(root.right)
        else:
            return root

    def find_parent(self, node):
        root = self.root
        parent = None
        if node.val == root.val:
            return
        while root:
            if root.val > node.val:
                parent = root
                root = root.left
            elif root.val < node.val:
                parent = root
                root = root.right
            elif root.val == node.val:
                return parent
        print('该元素不在树中')
        return

    def find_successor(self, root):
        if root.right is None:
            parent = self.find_parent(root)
            if parent is None:
                return
            while parent is not None and root == parent.right:
                root = parent
                parent = self.find_parent(root)
            return parent
        else:
            node = self.find_min(root.right)
            return node

    def delete_node(self, root, val):
        if self.search(val) is not True:
            print('要删除的点不在树中')
            return
        if val > root.val:
            # 要删除的点在右子树中
            root.right = self.delete_node(root.right, val)
        elif val < root.val:
            # 要删除的点在左子树中
            root.left = self.delete_node(root.left, val)
        else:
            # 要删除的点等于root
            if root.left and root.right:
                # root点的左右子树均不空
                temp = self.find_min(root.right)
                root.val = temp.val
                root.right = self.delete_node(root.right, temp.val)

            elif root.right is None and root.left is None:
                # root点的左右子树都是空
                root = None

            elif root.right and root.left is None:
                # root点只有右子树
                root = root.right

            elif root.left and root.right is None:
                # root点只有左子树
                root = root.left
        return root
