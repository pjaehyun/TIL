class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        output=""
        for i in s:
            if i.isalnum():
                output+=i
        if output==output[len(output)::-1]:
            return True
        else:
            return False