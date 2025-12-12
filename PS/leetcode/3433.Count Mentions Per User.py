class Solution:
    def countMentions(self, numberOfUsers: int, events: List[List[str]]) -> List[int]:
        events.sort(key=lambda x:(int(x[1]), x[0]=="MESSAGE"))
        answer = [0] * numberOfUsers

        offline = deque()
        offline_ids = {x:0 for x in range(numberOfUsers)}

        for message, timestamp, mention in events:

            while offline and offline[0][0] + 60 <= int(timestamp):
                curr = offline.popleft()
                if offline_ids[curr[1]] == 0: continue
                offline_ids[curr[1]] -= 1
            if message == "OFFLINE":
                _id = int(mention)
                offline_ids[_id] += 1
                offline.append(((int(timestamp), _id)))
            else:
                if mention == "ALL":
                    for i in range(len(answer)):
                        answer[i] += 1
                elif mention == "HERE":
                    for i in range(len(answer)):
                        if offline_ids[i] > 0: continue
                        answer[i] += 1
                else:
                    ids = mention.split()
                    for i in ids:
                        _id = int(i[2:])
                        answer[_id] += 1
        return answer