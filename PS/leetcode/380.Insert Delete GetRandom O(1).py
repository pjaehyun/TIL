# 첫번째 코드
class RandomizedSet:
    def __init__(self):
        self.randoms = set()

    def insert(self, val: int) -> bool:
        if val in self.randoms:
            return False
        self.randoms.add(val)
        return True

    def remove(self, val: int) -> bool:
        if val in self.randoms:
            self.randoms.remove(val)
            return True
        return False

    def getRandom(self) -> int:
        lst = list(self.randoms)
        num = random.randint(0,len(lst) - 1)
        return lst[num]

# 두번째 코드 
class RandomizedSet:
    def __init__(self):
        self.randoms = {}
        self.arr = []

    def insert(self, val: int) -> bool:
        if val in self.randoms: return False

        self.randoms[val] = len(self.arr)
        self.arr.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.randoms: return False
        last, idx = self.arr[-1], self.randoms[val]
        print(last, idx)
        self.arr[idx], self.randoms[last] = last, idx
        self.randoms.pop(val)
        self.arr.pop()
        return True
        

    def getRandom(self) -> int:
        return random.choice(self.arr)
    
# 세번째 코드
import random

class RandomizedSet:
    def __init__(self):
        self.random_set = []
        self.numbers = set()
        
    def insert(self, val: int) -> bool:
        if val not in self.numbers:
            self.random_set.append(val)
            self.numbers.add(val)
            return True
        return False

    def remove(self, val: int) -> bool:
        if val in self.numbers:
            self.random_set.remove(val)
            self.numbers.remove(val)
            return True
        return False

    def getRandom(self) -> int:
        random_idx = int(random.randrange(0, len(self.random_set)))
        return self.random_set[random_idx]
