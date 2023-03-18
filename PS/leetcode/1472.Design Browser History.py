class BrowserHistory:

    def __init__(self, homepage: str):
        self.history = [homepage]
        self.idx = 0

    def visit(self, url: str) -> None:
        self.history = self.history[:self.idx+1] + [url]
        self.idx = len(self.history) - 1

    def back(self, steps: int) -> str:
        if self.idx - steps < 0:
            self.idx = 0
        else:
            self.idx -= steps
        return self.history[self.idx]

    def forward(self, steps: int) -> str:
        if self.idx + steps >= len(self.history):
            self.idx = len(self.history) - 1
        else:
            self.idx += steps
        return self.history[self.idx]


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)