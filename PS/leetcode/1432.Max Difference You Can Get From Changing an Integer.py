class Solution:
    def maxDiff(self, num: int) -> int:
        max_value = num
        min_value = num
        num = str(num)

        for i in range(len(num)):
            if num[i] != '9':
                temp = num.replace(num[i], '9')
                max_value = int(temp)
                break

        if num[0] == '1':
            for i in range(1, len(num)):
                if num[i] not in "01":
                    temp = ''.join(num).replace(num[i], '0')
                    min_value = int(temp)
                    break
        else:
            temp = ''.join(num).replace(num[0], '1')
            min_value = int(temp)

        return max_value - min_value
        