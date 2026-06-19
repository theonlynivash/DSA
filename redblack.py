RED = True
BLACK = False
class Node:
    def __init__(self, data):
        self.data = data
        self.color = RED
        self.left = None
        self.right = None
        self.parent = None
class RBTree:
    def __init__(self):
        self.NULL = Node(0)
        self.NULL.color = BLACK
        self.root = self.NULL
    def insert(self, data):
        node = Node(data)
        node.left = self.NULL
        node.right = self.NULL
        parent = None
        current = self.root
        while current != self.NULL:
            parent = current
            if node.data < current.data:
                current = current.left
            else:
                current = current.right
        node.parent = parent
        if parent is None:
            self.root = node
        elif node.data < parent.data:
            parent.left = node
        else:
            parent.right = node
        self.fix(node)
    def fix(self, node):
        while node.parent and node.parent.color == RED:
            if node.parent == node.parent.parent.left:
                uncle = node.parent.parent.right
                if uncle.color == RED:          # Case 1: Recolor
                    node.parent.color = BLACK
                    uncle.color = BLACK
                    node.parent.parent.color = RED
                    node = node.parent.parent
                else:
                    if node == node.parent.right:  # Case 2: Left Rotate
                        node = node.parent
                        self.leftrotate(node)
                    node.parent.color = BLACK      # Case 3: Right Rotate
                    node.parent.parent.color = RED
                    self.rightrotate(node.parent.parent)
            else:
                uncle = node.parent.parent.left
                if uncle.color == RED:          # Case 1: Recolor
                    node.parent.color = BLACK
                    uncle.color = BLACK
                    node.parent.parent.color = RED
                    node = node.parent.parent
                else:
                    if node == node.parent.left:   # Case 2: Right Rotate
                        node = node.parent
                        self.rightrotate(node)
                    node.parent.color = BLACK      # Case 3: Left Rotate
                    node.parent.parent.color = RED
                    self.leftrotate(node.parent.parent)
        self.root.color = BLACK
    def leftrotate(self, z):
        y = z.right
        z.right = y.left
        if y.left != self.NULL:
            y.left.parent = z
        y.parent = z.parent
        if z.parent is None:
            self.root = y
        elif z == z.parent.left:
            z.parent.left = y
        else:
            z.parent.right = y
        y.left = z
        z.parent = y
    def rightrotate(self, z):
        y = z.left
        z.left = y.right
        if y.right != self.NULL:
            y.right.parent = z
        y.parent = z.parent
        if z.parent is None:
            self.root = y
        elif z == z.parent.right:
            z.parent.right = y
        else:
            z.parent.left = y
        y.right = z
        z.parent = y
    def inorder(self, node):
        if node != self.NULL:
            self.inorder(node.left)
            c = "R" if node.color == RED else "B"
            print(f"{node.data}({c})", end=" ")
            self.inorder(node.right)

# ---- Main ----
rbt = RBTree()
for val in [10, 20, 30, 40, 50]:
    rbt.insert(val)

print("Inorder:")
rbt.inorder(rbt.root)