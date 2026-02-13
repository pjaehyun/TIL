class Solution:
    def longestBalanced(self, s: str) -> int:
        n=len(s)
        ans, Len=1, 1
        for c0, c1 in pairwise(s):
            if c0==c1: Len+=1
            else:
                ans=max(ans, Len)
                Len=1
        ans=max(ans, Len)

        ab, bc, ca, abc={},{},{},{}
        abc[(0, 0)]=ab[(0, 0)]=bc[(0, 0)]=ca[(0, 0)]=-1

        cnt=[0, 0, 0]
        for i, c in enumerate(s):
            cnt[ord(c)-97]+=1
            A, B, C=cnt

            key=(B-A, C-A)
            if  key in abc: ans=max(ans, i-abc[key])
            else: abc[key]=i

            key=(A-B, C)
            if  key in ab: ans=max(ans, i-ab[key])
            else: ab[key]=i

            key=(B-C, A)
            if  key in bc: ans=max(ans, i-bc[key])
            else: bc[key]=i

            key=(C-A, B)
            if  key in ca: ans=max(ans, i-ca[key])
            else: ca[key]=i
        return ans    