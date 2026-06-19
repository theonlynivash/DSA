class Node:
    def __init__(self,data):
        self.data = data
        self.right  = None
        self.left = None
        self.height = 1
class AVL:
    def __init__(self,root):
        self.root = Node(root)
    def h(self,node):
        if not node:
            return 0 
        return node.height
    def bf(self,node):
        if not node:
            return 0 
        return self.h(node.left) - self.h(node.right)
    def r_ll(self,z):
        y = z.left
        t = y.right
        y.right = z
        z.left = t
        z.height = 1+max(self.h(z.left),self.h(z.right))
        y.height = 1+max(self.h(y.left),self.h(y.right))
        return y
    def l_rr(self,z):
        y = z.right
        t = y.left
        y.left = z
        z.right = t
        z.height = 1+max(self.h(z.left),self.h(z.right))
        y.height = 1+max(self.h(y.left),self.h(y.right))
        return y
    def insert(self,node,data):
        if data > node.data :
            if node.right == None:
                node.right = Node(data)
            else:
                node.right = self.insert(node.right,data)
        if data < node.data :
            if node.left == None :
                node.left = Node(data)
            else:
                node.left = self.insert(node.left,data)
        node.height = 1 + max(self.h(node.left), self.h(node.right))
        balance = self.h(node.left) - self.h(node.right)

        if balance > 1 and data < node.left.data:
            return self.r_ll(node)
        elif balance > 1 and data > node.left.data:
            node.left = self.l_rr(node.left)
            return self.r_ll(node)
        elif balance < -1 and data < node.right.data:
            node.right = self.r_ll(node.right)
            return self.l_rr(node)
        elif balance < -1 and data > node.right.data:
            return self.l_rr(node)
        
        return node
    
    def inorder(self,node):
        if node:
            self.inorder(node.left)
            print(node.data,end=" ")
            self.inorder(node.right)
a = AVL(40)
a.root = a.insert(a.root, 30)   # ← missing a.root =
a.root = a.insert(a.root, 20)
a.root = a.insert(a.root, 10)
a.inorder(a.root)