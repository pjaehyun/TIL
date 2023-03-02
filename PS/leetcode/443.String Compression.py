class Solution:
    def compress(self, chars: List[str]) -> int:
        if len(chars) == 1:
            return 1
        
        i, j = 0, 1
        while j < len(chars):
            if chars[i] == chars[j]:
                j += 1
            else:
                if len(chars[i:j]) > 1:
                    comp = chars[i:i+1] + list(str(len(chars[i:j])))
                    chars[i:j] = comp
                    i += len(comp)
                    j = i + 1
                else:
                    chars[i:j] = chars[i:i+1]
                    i += 1
                    j = i + 1
        if len(chars[i:j]) > 1:
            chars[i:j] = chars[i:i+1] + list(str(len(chars[i:j])))

        return len(chars)