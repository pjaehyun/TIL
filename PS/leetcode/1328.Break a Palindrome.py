# 첫번째 코드
class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        palindrome = list(palindrome)
        if len(palindrome) == 1:
            return ""
        for i in range(len(palindrome)):
            if palindrome[i] != 'a':
                temp = palindrome[i]
                palindrome[i] = 'a'
                _isPalindrome = isPalindrome(palindrome)
                if _isPalindrome:
                    palindrome[i] = temp
                    continue
                else:
                    break
            if i == (len(palindrome) - 1):
                if palindrome[i] == 'a':
                    palindrome[i] = chr(97 + 1)
        return ''.join(palindrome)

def isPalindrome(s):
    reverse = s[::-1]
    if s == reverse:
        return True
    else:
        return False

# 개선 코드 
class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        palindrome = list(palindrome)
        if len(palindrome) == 1:
            return ""
            
        for i in range(len(palindrome) // 2):
            if palindrome[i] != 'a':
                palindrome[i] = 'a'
                return ''.join(palindrome)
        palindrome[-1] = 'b'
        return ''.join(palindrome)
