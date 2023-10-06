class Solution:
    def integerBreak(self, n: int) -> int:
        if n == 2:
            return 1
        if n == 3:
            return 2

        max_product = [0] * (n + 1)

        max_product[1] = 1
        max_product[2] = 2
        max_product[3] = 3

        for num in range(4, n + 1):
            max_product_for_num = 0
            for sub_num in range(1, num // 2 + 1):
                max_product_for_num = max(max_product_for_num, max_product[sub_num] * max_product[num - sub_num])
            max_product[num] = max_product_for_num

        return max_product[n]