class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        answer = []
        
        pack = []
        pack_len = 0
        for word in words:
            if pack_len + len(word) + len(pack) - 1 < maxWidth:
                pack_len += len(word)
                pack.append(word)
            else:
                spacing_count = len(pack) - 1
                spacing = ["" for _ in range(spacing_count)]
                res = ""
                if spacing_count > 0:
                    for i in range(maxWidth - pack_len):
                        spacing[i % spacing_count] += " "
                    for i in range(len(pack) - 1):
                        res += pack[i] + spacing[i]
                    res += pack[-1]
                else:
                    res = pack[0] + (" " * (maxWidth - pack_len))
                answer.append(res)
                pack = [word]
                pack_len = len(word)
        temp = ' '.join(pack)
        answer.append(temp + " " * (maxWidth - len(temp)))
        return answer