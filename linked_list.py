
class Node:
    # called when you do Node(10)
    def __init__(self, data):
        self.data = data    # stores the value e.g. 10
        self.next = None   # no next node yet

class LinkedList:
    def __init__(self):
        self.head = None   # empty list — no nodes yet
 
    def append(self, data):
        new_node = Node(data)      # create new node
        if not self.head:           # list is empty?
            self.head = new_node    # new node becomes head
            return
        current = self.head         # start at the first node
        while current.next:        # walk until last node
            current = current.next
        current.next = new_node     # attach at the end

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head   # new node points to old head
        self.head = new_node        # new node is now the head
 
    def delete(self, data):
        if not self.head:           # list is empty, nothing to do
            return
        if self.head.data == data:  # deleting the head node?
            self.head = self.head.next  # 2nd node becomes new head
            return
        current = self.head
        while current.next:        # walk the list
            if current.next.data == data: # found it?
                current.next = current.next.next  # skip over it
                return
            current = current.next
 
    def search(self, data):
        current = self.head
        while current:             # visit every node
            if current.data == data:
                return True        # found!
            current = current.next
        return False               # not found
 
    def display(self):
        current = self.head
        while current:             # visit every node
            print(current.data, end=" -> ")
            current = current.next
        print("None")               # mark end of list
 
ll = LinkedList()              # create empty list
ll.append(10)                  # 10 -> None
ll.append(20)                  # 10 -> 20 -> None
ll.append(30)                  # 10 -> 20 -> 30 -> None
ll.prepend(5)                  # 5 -> 10 -> 20 -> 30 -> None
ll.display()                   # prints it
print(ll.search(20))           # True
print(ll.search(99))           # False
ll.delete(20)                  # remove 20
ll.display()                   # prints updated list
