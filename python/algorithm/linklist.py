# -*-coding:utf-8-*-
"""
创建带头结点的单项链表
head->LinkNode->LinkNode
实例化操作为a = LinkList()
=============================
isEmpty()                  判断是否为空,空则返回True，不空则返回False
initlist_tail(data)        将list转换为链表
travel()                   顺序输出链表
length()                   返回链表中除取头结点的节点个数
search(item)               查找元素，有则返回其位置，无则返回False
insertElem(key, index)     在index位置插入元素key，并顺序输出插入后的链表
deleteIndex(index)         删除index位置的元素，并顺序输出删除元素后的链表
reverseList()              反转链表
clear()                    清空链表
=============================
example:
=============================
data = [1, 2, 3, 4, 5]
l = LinkList()
print(l.length())
print(l.isEmpty())
l.initlist_tail(data)
l.travel()
print(l.search(4))
l.insertElem(10, 4)
print(l.length())
l.deleteIndex(6)
l.reverseList()
l.travel()
l.clear()
print(l.length())
============================
"""


class LinkNode(object):
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkList(object):
    def __init__(self):
        self.head = LinkNode(None)

    def initlist_tail(self, data):
        p = self.head
        p.next = LinkNode(data[0])
        p = p.next
        for i in data[1:]:
            node = LinkNode(i)
            p.next = node
            p = p.next

    def isEmpty(self):
        if self.head.next:
            return False
        else:
            return True

    def travel(self):
        if self.isEmpty():
            print('Empty LinkList')
            return
        else:
            p = self.head.next
            while p:
                print(p.data, end=',')
                p = p.next
        print()

    def length(self):
        if self.isEmpty():
            return 0
        else:
            num = 0
            p = self.head.next
            while p:
                num += 1
                p = p.next
            return num

    def search(self, item):
        p = self.head.next
        num = 1
        while p:
            if p.data != item:
                p = p.next
                num += 1
            else:
                return num
        # print('查找不到此元素')
        return None

    def insertElem(self, key, index):
        if index < 1 or index > self.length():
            print('插入位置超范围')
            exit(0)
        else:
            p = self.head
            j = 1
            while p and j < index:
                p = p.next
                j += 1

            node = LinkNode(key)
            node.next = p.next
            p.next = node
            print('inserted LinkList:')
            self.travel()

    def deleteIndex(self, index):
        if index < 1 or index > self.length():
            print('删除位置错误')
        else:
            p = self.head
            j = 1
            while p and j < index:
                p = p.next
                j += 1
            p.next = p.next.next
            print('deleted LinkList:')
            self.travel()

    def reverseList(self):
        h = self.head
        p = p1 = self.head.next
        self.head.next = None
        while p:
            flag = p.next
            p.next = h
            h = p
            p = flag
        p1.next = None
        self.head = LinkNode(None)
        self.head.next = h

    def clear(self):
        self.head.next = None
