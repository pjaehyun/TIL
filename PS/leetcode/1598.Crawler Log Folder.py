class Solution:
    def minOperations(self, logs: List[str]) -> int:
        step = 0

        for command in logs:
            if command == "../":
                step = max(0, step - 1)
            elif command == "./":
                continue
            else:
                step += 1
        return step