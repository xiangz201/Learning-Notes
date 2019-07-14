# -*-coding:utf-8-*-
"""
用list实现栈
实例化操作为a = Stack()
=============================
isEmpty() 判断是否为空,空则返回True，不空则返回False
push()    压入元素
pop()     弹出元素
peek()    返回最顶层元素，但不删除它
size()    返回栈内元素的个数
=============================
example:
=============================
a = Stack()
length = a.size()
a.push(1)
top = a.peek()
a.pop()
============================
"""


class Stack(object):
    def __init__(self):
        self.stack = []

    def isEmpty(self):
        return self.stack == []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if self.isEmpty():
            raise IndexError('pop from empty stack')
        else:
            return self.stack.pop()

    def peek(self):
        if self.isEmpty():
            raise IndexError('peek from empty stack')
        else:
            return self.stack[-1]

    def size(self):
        return len(self.stack)
