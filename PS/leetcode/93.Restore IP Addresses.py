class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        
        answer = []

        def backtracking(s, idx, ip):
            if len(ip) == 4 and idx == len(s):
                answer.append('.'.join(ip[:]))

            for i in range(0, 3):
                if idx + i >= len(s):
                    break
                temp = s[idx:idx+i+1]
                if (int(temp) < 0 or int(temp) > 255) or (len(temp) >= 2 and temp[0] == "0"):
                    return
                ip.append(temp)
                backtracking(s, idx + i +1, ip)
                ip.pop()
        
        backtracking(s, 0, [])
        return answer
        