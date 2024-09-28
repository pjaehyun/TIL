from collections import deque

class MyCircularDeque(object):
    def __init__(self, k):
        self.dq = deque()
        self.n = k

    def insertFront(self, value):
        if len(self.dq) < self.n:
            self.dq.appendleft(value)
            return True
        return False

    def insertLast(self, value):
        if len(self.dq) < self.n:
            self.dq.append(value)
            return True
        return False

    def deleteFront(self):
        if self.dq:
            self.dq.popleft()
            return True
        return False

    def deleteLast(self):
        if self.dq:
            self.dq.pop()
            return True
        return False

    def getFront(self):
        return -1 if not self.dq else self.dq[0]

    def getRear(self):
        return -1 if not self.dq else self.dq[-1]

    def isEmpty(self):
        return len(self.dq) == 0

    def isFull(self):
        return len(self.dq) == self.n