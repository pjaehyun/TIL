class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:

        curr_time = customers[0][0] + customers[0][1]
        wait_time = customers[0][1]

        for i in range(1, len(customers)):
            if curr_time < customers[i][0]:
                curr_time = customers[i][0] + customers[i][1]
            else:
                curr_time += customers[i][1]
            wait_time += (curr_time - customers[i][0])
        return wait_time / len(customers)