# -*-coding:utf-8-*-
"""
二叉搜索树的插入，删除，查询操作
=============================
left_rotate(x: RBNode)          节点x上做左旋
right_rotate(x: RBNode)         节点x上做右旋
rb_insert( z: RBNode)           插入节点z
delete_index(z: RBNode)         删除节点z
=============================
红黑树的5个性质
特征一： 节点要么是红色，要么是黑色（红黑树名字由来）。
特征二： 根节点是黑色的
特征三： 每个叶节点(nil或空节点)是黑色的。
特征四： 每个红色节点的两个子节点都是黑色的（相连的两个节点不能都是红色的）。
特征五： 从任一个节点到其每个叶子节点的所有路径都是包含相同数量的黑色节点。
从五大特征直观上总结出来几个点：
1 对每个红色节点，子节点只有两种情况：要么都没有，要么都是黑色的。（不然会违反特征四）
2 对黑色节点，如果只有一个子节点，那么这个子节点，必定是红色节点。（不然会违反特征五）
3 假设从根节点到叶子节点中，黑色节点的个数是h, 那么树的高度H范围 h<= H <= 2H（特征四五决定）。
红黑树的插入：
同二叉搜索树的插入，为保持性质，在加上一次调整
（1）z在祖父节点的左侧
1 如果插入节点的父节点是黑色，则无需调整
2 如果插入节点的父节点是红色
  一、z的叔叔节点是红色     case1
  二、z的叔叔节点是黑色
    一、z在父节点的右侧    case2
        进行一些变化转为情况二
    二、z在父节点的左侧    case3
（2）z在祖父节点的右侧
    对称操作
红黑树的删除:
桶二叉搜索树的删除，同样要进行调整
1 如果删除的点是红色，则无需调整
（1）x在父节点的左侧
1 如果删除的点是黑色，则最底部发生位置变动的点x开始调整
  一、x点兄弟节点是红色        case1
  二、x点的兄弟节点w是黑色
    一、w的两个子节点都是黑色   case2
       w节点变为红色，x上移为x的双亲
    二、w的左子节点为红色，右子节点为黑色  case3
       右旋操作
    三、w的右子节点为红色     case4
       x设为根节点
============================
"""


class RBNode(object):
    def __int__(self, val=None, color='B', left=None, right=None, parent=None):
        self.val = val
        self.color = color
        self.left = left
        self.right = right
        self.parent = parent


class RBTree(object):
    def __init__(self):
        self.root = None
        self.ls = [[] for _ in range(10)]

    def left_rotate(self, x: RBNode):
        y = x.right
        x.right = y.left
        if y.left is not None:
            x.right.parent = x
        if x.parent is None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        elif x == x.parent.right:
            x.parent.right = y
        y.left = x
        x.parent = y

    def right_rotate(self, x: RBNode):
        y = x.left
        x.left = y.right
        if y.right is not None:
            x.left.parent = x
        if x.parent.left == x:
            x.parent.left = y
        elif x.parent.right == x:
            x.parent.right = y
        y.right = x
        x.parent = y

    def rb_insert(self, z: RBNode):
        y = None
        x = self.root
        while x is not None:
            y = x
            if z.value < x.value:
                x = x.left
            else:
                x = x.right
        z.parent = y
        if y is None:
            self.root = z
        elif z.value < y.value:
            y.left = z
        else:
            y.right = z
        z.left = None
        z.right = None
        z.color = 'R'
        self.rb_index_fixup(z)

    def rb_index_fixup(self, z: RBNode):
        # while z.parent.color == 'R':
        if z.parent == z.parent.parent.left:
            while z.parent.color == 'R':
                y = z.parent.parent.right
                if y.color == 'R':                     #case1
                    z.parent.color = 'B'               #case1
                    y.color = 'B'                      #case1
                    z.parent.parent.color = 'R'        #case1
                    z = z.parent.parent                #case1
                elif z == z.parent.right:              #case2
                    z = z.parent                       #case2
                    self.left_rotate(z)                #case2
                else:
                    z.parent.color = 'B'               #case3
                    z.parent.parent.color = 'R'        #case3
                    self.right_rotate(z.parent.parent) #case3
        if z.parent == z.parent.parent.right:
            while z.parent.color == 'R':
                y = z.parent.parent.left
                if y.color == 'R':
                    z.parent.color = 'B'
                    y.color = 'B'
                    z.parent.parent.color = 'R'
                    z = z.parent.parent
                elif z == z.parent.left:
                    z = z.parent
                    self.right_rotate(z)
                else:
                    z.parent.color = 'B'
                    z.parent.parent.color = 'R'
                    self.left_rotate(z.parent.parent)
        self.root.color = 'B'

    def rb_transplant(self, old_son_tree: RBNode, new_son_stree: RBNode):
        if old_son_tree.parent is None:
            self.root = new_son_stree
        elif old_son_tree == old_son_tree.parent.left:
            old_son_tree.parent.left = new_son_stree
        elif old_son_tree == old_son_tree.parent.right:
            old_son_tree.parent.right = new_son_stree
        new_son_stree.parent = old_son_tree.parent

    def rb_minmum(self, z: RBNode):
        while z.left is not None:
            z = z.left
        return z

    def delete_index(self, z: RBNode):
        y = z
        y_original_color = y.color
        if z.left is None:
            x = z.left
            self.rb_transplant(z, z.left)
        elif z.right is None:
            x = z.left
            self.rb_transplant(z, z.right)
        else:
            y = self.rb_minmum(z.right)
            y_original_color = y.color
            x = y.right
            if y.parent == z:
                x.parent = y
            else:
                self.rb_transplant(y, y.right)
                y.right = z.right
                y.right.parent = y
            self.rb_transplant(z, y)
            y.left = z.left
            y.left.parent = y
            y.color = z.color
        if y_original_color == 'B':
            self.rb_delete_fixup(x)
        #

    def rb_delete_fixup(self, x: RBNode):
        if x == x.parent.left:
            while x != self.root and x.color == 'B':
                w = x.parent.right
                if w.color == 'R':                  #case1
                    w.color = 'B'                   #case1
                    x.parent.color = 'R'            #case1
                    self.left_rotate(x.parent)      #case1
                    w = x.parent.right              #case1
                elif w.color == 'B' and w.left.color == 'B' and w.right.color == 'B':        #case2
                    w.color = 'R'                   #case2
                    x = x.parent                    #case2
                elif w.color == 'B' and w.right.color == 'B' and w.left.color == 'R':        #case3
                    w.left.color = 'B'              #case3
                    w.color = 'R'                   #case3
                    self.right_rotate(w)            #case3
                    w = x.parent.right              #case3
                elif w.color == 'B' and w.right.color == 'R':                                #case3
                    w.color = x.parent.color        #case4
                    x.parent.color = 'B'            #case4
                    w.right.color = 'B'             #case4
                    self.left_rotate(x.parent)      #case4
                    x = self.root                   #case4
        if x == x.parent.right:
            while x != self.root and x.color == 'B':
                w = x.parent.left
                if w.color == 'R':
                    w.color = 'B'
                    x.parent.color = 'R'
                    self.right_rotate(x.parent)
                    w = x.parent.left
                elif w.color == 'B' and w.left.color == 'B' and w.right.color == 'B':
                    w.color = 'R'
                    x = x.parent
                elif w.color == 'B' and w.left.color == 'B' and w.right.color == 'R':
                    w.right.color = 'B'
                    w.color = 'R'
                    self.left_rotate(w)
                    w= x.parent.left
                elif w.color == 'B' and w.left.color == 'R':
                    w.color = x.parent.color
                    x.parent.color = 'B'
                    self.right_rotate(x.parent)
                    x = self.root
        x.color = 'B'