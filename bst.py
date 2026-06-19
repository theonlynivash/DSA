class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
class bst:
    def __init__(self,root):
        self.root = Node(root)
    def insert(self,node,data):
        if node.data > data:
            if node.left == None:
                node.left = Node(data)
            else:
                self.insert(node.left,data)
        elif node.data<data:
            if node.right==None:
                node.right = Node(data)
            else:
                self.insert(node.right,data)
    def search(self,node,data):
        if node == None:
            return False
        if node.data == data:
            return True
        elif node.data<data:
            return self.search(node.right,data)
        elif node.data>data:
            return self.search(node.left,data)
    def inorder(self,node):
        if node:
            self.inorder(node.left)
            print(node.data)
            self.inorder(node.right)
    def prorder(self,node):
        if node :
            print(node.data)
            self.prorder(node.left)
            self.prorder(node.right)
    def postorder(self, node):
        if node:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.data)
bst1 = bst(10)
bst1.insert(bst1.root,5)
bst1.insert(bst1.root,15)
bst1.insert(bst1.root,3)
bst1.insert(bst1.root,7)
bst1.insert(bst1.root,12)
bst1.insert(bst1.root,18)
print(bst1.search(bst1.root,7))
print(bst1.search(bst1.root,20))
print("Inorder Traversal:")
bst1.inorder(bst1.root)
print("Preorder Traversal:")
bst1.prorder(bst1.root)
print("Postorder Traversal:")
bst1.postorder(bst1.root)
