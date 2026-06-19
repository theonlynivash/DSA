from collections import deque
class mydeque:
    def __init__(self):
        self.dq = deque()
    def is_empty(self):
        return (len(self.dq) == 0)
    def add_front(self,item):
        self.dq.appendleft(item)
    def add_rear(self,item):
        self.dq.append(item)
    def remove_front(self):
        self.dq.popleft()
    def reomve_rear(self):
        self.dq.pop()
    def display(self):
        print(list(self.dq))
dq1 = mydeque()
dq1.add_front(0)
dq1.add_front(1)
dq1.add_front(2)
dq1.add_rear(97)
dq1.add_rear(98)
dq1.add_rear(99)
dq1.display()