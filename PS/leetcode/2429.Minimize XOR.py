class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        num1_to_bin = str(bin(num1))[2:]
        num2_one_count = Counter(bin(num2))['1']
        
        x = deque()
        for i in range(len(num1_to_bin)):
            if num1_to_bin[i] == '1' and num2_one_count > 0:
                x.append('1')
                num2_one_count -= 1
            else:
                x.append('0')

        for i in range(len(x) - 1, -1, -1):
            if x[i] == '0' and num2_one_count > 0:
                x[i] = '1'
                num2_one_count -= 1

        for i in range(num2_one_count):
            x.appendleft('1')
        answer = 0

        for i in range(len(x)):
            if x[i] == '1':
                answer += 2**(len(x) - (i+1))
        return answer
