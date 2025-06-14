class Solution:
    def minMaxDifference(self, num: int) -> int:
        s = str(num)
        
        firstNon9 = re.search(r'[0-8]', s)
        firstNon0 = re.search(r'[1-9]', s)
        
        max_num = int(s.replace(s[firstNon9.start()], '9')) if firstNon9 else num
        min_num = int(s.replace(s[firstNon0.start()], '0')) if firstNon0 else num
        
        return max_num - min_num