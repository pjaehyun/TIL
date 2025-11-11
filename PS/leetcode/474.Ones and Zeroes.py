class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        
        dp = {(0, 0): 0}

        for s in strs:
            ones = s.count('1')
            zeroes = s.count('0')

            n_dp = {}

            for k, v in dp.items():
                pz, po = k

                nz, no = pz + zeroes, po + ones
                if nz <= m and no <= n:
                    if (nz, no) not in dp:
                        n_dp[(nz, no)] = v + 1
                    elif dp[(nz, no)] < v + 1:
                        n_dp[(nz, no)] = v+1
            dp.update(n_dp)
        return max(dp.values())