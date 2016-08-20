# -*- coding: utf-8 -*-
__author__ = 'cyf'

"""
**************************
测试用的树如下图所示：(图略丑QAQ)
              1
            /  \     \
           /    \     \
          2      3     4
        / \ \   / \ \
        5 6 7   8 9 10
                   \
                   11
**************************
"""

class Tree(object):

    def __init__(self, root=None):
        self.key = root
        self.childTree = []  # 子树的集合

    def add(self, k, v):
        """k是父节点，v是子节点"""
        if not self.key:
            print 'This tree is None,now the %s will be the root!' % k
            self.key = k
            v_t = Tree(v)
            self.childTree.append(v_t)
        else:
            k_t = Tree.find(self, k)
            for node in k_t.childTree:
                if node.key == v:  # v已经是k的子节点
                    print "the %d has been already the child of %d!" % (v, k)
                    return False
            v_t = Tree(v)
            k_t.childTree.append(v_t)

    @staticmethod
    def find(root, k):
        """找到父节点k"""
        if root.key == k:
            return root
        temp = [node for node in root.childTree]
        while len(temp) > 0:
            child = temp[-1]
            if child.key == k:
                return child
            temp.pop()
            temp.extend(node for node in child.childTree)
        return None

    def get(self, k):
        """根据父节点k，获得所有叶子结点"""
        leaves = []
        k_t = Tree.find(self, k)
        if not k_t:  # 没有找到父节点k
            print 'there is no %d node!' % k
            return False
        if len(k_t.childTree) < 1:  # 父节点k本身就是个叶子节点
            leaves.append(k_t)
            return leaves
        temp = [k_t]  # 父节点k不是叶子节点
        while len(temp) > 0:
            node = temp[-1]
            temp.pop()
            for item in node.childTree:
                if len(item.childTree) > 0:
                    temp.append(item)
                else:
                    leaves.append(item)
        return leaves


def printf(t_l):
    """由于返回的都是包含对象的列表，很难看清结果，可以利用printf函数来输出树节点的key值"""
    print "[",
    for i in t_l:
        print i.key,
    print "]"

if __name__ == '__main__':
    # 以下为测试数据
    t = Tree()
    t.add(1, 2)
    t.add(1, 2)
    t.add(1, 3)
    t.add(1, 4)
    t.add(2, 5)
    t.add(2, 6)
    t.add(2, 7)
    t.add(3, 8)
    t.add(3, 9)
    t.add(3, 10)
    t.add(9, 11)
    r = t.get(1)
    printf(r)
