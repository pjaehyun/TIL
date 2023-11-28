class Solution:
    def numberOfWays(self, corridor: str) -> int:
        chairs = 0
        plants = 0
        answer = 1

        for c in corridor:
            if c == "S":
                chairs += 1

                if chairs % 2 == 1 and plants != 0:
                    answer *= (plants+1)
                    plants = 0
            else:
                if chairs and chairs % 2 == 0:
                    plants += 1
        return answer%(10**9+7) if chairs and chairs%2 == 0 else 0