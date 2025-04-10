class Solution:
    def numberOfPowerfulInt(self, start: int, finish: int, limit: int, s: str) -> int:
        s_start = str(start - 1)
        s_finish = str(finish)
        
        return self.count_powerful(s_finish, s, limit) - self.count_powerful(s_start, s, limit)
    
    def count_powerful(self, num: str, suffix: str, limit: int) -> int:
        if len(num) < len(suffix):
            return 0
            
        if len(num) == len(suffix):
            return 1 if num >= suffix else 0
        
        result = 0
        prefix_len = len(num) - len(suffix)
        
        for i in range(prefix_len):
            digit = int(num[i])
            
            if digit > limit:
                result += (limit + 1) ** (prefix_len - i)
                return result
                
            result += digit * (limit + 1) ** (prefix_len - i - 1)
        
        if num[-len(suffix):] >= suffix:
            result += 1
            
        return result