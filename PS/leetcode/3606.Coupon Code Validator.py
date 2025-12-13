class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        n = len(code)

        codes = []

        for i in range(n):
            if businessLine[i] in ["electronics", "grocery", "pharmacy", "restaurant"] and isActive[i]:
                if code[i] == "": continue 
                special = re.findall(r'[\W]', code[i])
                if not special:
                    codes.append((code[i], businessLine[i]))
        codes.sort(key=lambda x: (x[1], x[0]))
        return [a for a, b in codes]
        