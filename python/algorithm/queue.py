# -*-coding:utf-8-*-
"""
自己实现队列
建立头结点类和节点类
队列有一个头结点，头结点左边指向最后一个元素，头结点右边指向第一个元素
节点类有一个指针指向下一个元素，一个指针指向value
实例化操作为a = Queue()
=============================
isEmpty()          判断是否为空,空则返回True，不空则返回False
enqueue(object)    入队
dequeue(object)    出队
top()              返回最顶层元素，但不删除它
size()             返回队列内元素的个数
=============================
example:
=============================
a = Queue()
length = a.size()
a.enqueue(1)
a.enqueue(12)
length = a.size()
top = a.top()
a.dequeue()
============================
"""


class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None


class Head(object):
    def __init__(self):
        self.right = None
        self.left = None


class Queue(object):
    def __init__(self):
        self.head = Head()

    def enqueue(self, value):
        new_node = Node(value)
        p = self.head
        if p.left:
            # 队列已经有了元素
            temp = p.left
            p.left = new_node
            temp.next = new_node
        else:
            # 队列空
            p.right = new_node
            p.left = new_node

    def dequeue(self):
        p = self.head
        if p.right and p.left == p.right:
            # 队列只有一个元素
            temp = p.right
            p.right = p.left = None
            return temp.value
        elif p.right and (p.left != p.right):
            # 队列有多个元素
            temp = p.right
            p.right = temp.next
            return temp.value
        else:
            # 队列为空
            raise LookupError('queue is empty')

    def size(self):
        p = self.head
        num = 1
        if self.isEmpty():
            # 队列为空
            return 0
        else:
            # 队列有多个元素
            temp = p.right
            while temp.next:
                temp = temp.next
                num += 1
            return num

    def isEmpty(self):
        if self.head.right:
            return False
        else:
            return True

    def top(self):
        if self.head.right:
            return self.head.right.value
        else:
            raise LookupError('queue is empty')

#测试用例
#a = Queue()
#a.enqueue(12)
#a.enqueue(21)
#print(a.top(), a.size())
#print(a.dequeue,a.size())
