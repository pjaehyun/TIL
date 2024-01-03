class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        answer = 0

        curr = 0

        for i in range(len(bank)):
            razer_count = bank[i].count("1")
            if razer_count == 0:
                continue
            answer = answer + (razer_count * curr)
            curr = razer_count
        return answer