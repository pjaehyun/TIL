# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        min_value = 1
        max_value = n
        while min_value <= max_value:
            pick = (min_value + max_value) // 2
            response = guess(pick)

            if response == 0:
                return pick
            elif response == -1:
                max_value = pick - 1
            else:
                min_value = pick + 1
        