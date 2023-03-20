# 첫번째 풀이
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if len(flowerbed) == 1:
            if flowerbed[0] == 0:
                return True if 1 >= n else False
            else:
                return True if 0 >= n else False
        count = 0 
        i = 0
        while i < len(flowerbed):
            if i == 0 and flowerbed[i] == 0 and flowerbed[i+1] == 0:
                flowerbed[i] = 1
                count += 1
                i += 1
            elif i == len(flowerbed) - 1 and flowerbed[i] == 0 and flowerbed[i-1] == 0:
                flowerbed[i] = 1
                count += 1
                i += 1
            elif flowerbed[i] == 0 and flowerbed[i-1] == 0 and flowerbed[i+1] == 0:
                flowerbed[i] = 1
                count += 1
                i += 1
            else:
                i += 1

        return True if count >= n else False
            
# 두번째 풀이(시간복잡도 및 코드 개선)
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        flowerbed = [0] + flowerbed + [0]
        count = 0 

        for i in range(1, len(flowerbed)-1):
            if flowerbed[i] == 0 and flowerbed[i-1] == 0 and flowerbed[i+1] == 0:
                flowerbed[i] = 1
                count += 1

        return True if count >= n else False