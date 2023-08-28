class MyStack:

    def __init__(self):
        self.myStack = deque()

    def push(self, x: int) -> None:
        self.myStack.append(x)
        for _ in range(len(self.myStack) - 1):
            self.myStack.append(self.myStack.popleft())

    def pop(self) -> int:
        return self.myStack.popleft()

    def top(self) -> int:
        return self.myStack[0]

    def empty(self) -> bool:
        return True if not self.myStack else False


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()