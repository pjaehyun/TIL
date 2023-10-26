class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        # i**0.5 < j sqrt(i)가 작다면 j보다 큰수를 곱했을 때 결과가 안나오게됨 그럼 이걸론 tree를 생성할 수 없다
        # i % j == 0 i를 j로 나눴을때 나머지가 0이고 
        # i // j in s 나눈 몫이 s에 있다면 j * s = i가 된다 그러므로 트리를 만들 수 있음 
        # i // j == j 라면 j*j=i가 되기때문에 dp[i] += dp[j] * dp[j]
        # 그게아니면 j*s=i가 되기때문에 dp[i] += dp[j] * dp[i//j] * 2 여기서 *2는 순서가 바뀌었을 때도 가능하기 때문에 추가

        arr.sort()
        s = set(arr)
        dp = {x:1 for x in arr}

        for i in arr:
            for j in arr:
                if j > i**0.5:
                    break
                else:
                    if i % j == 0 and i // j in s:
                        if i // j == j:
                            dp[i] += dp[j] * dp[j]
                        else:
                            dp[i] += dp[j] * dp[i//j] * 2
                    dp[i] = dp[i] % (10**9 + 7)
        return sum(dp.values()) % (10**9 + 7)