# 해결하지못함
class Solution:
    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
        groupId = m
        for i in range(n):
            if group[i] == -1:
                group[i] = groupId
                groupId += 1
        
        itemGraph = defaultdict(list)
        itemIndegree = [0] * n
        groupGraph = defaultdict(list)
        groupIndegree = [0] * groupId

        for i in range(n):
            for prev in beforeItems[i]:
                itemGraph[prev].append(i)
                itemIndegree[i] += 1
                if group[i] != group[prev]:
                    groupGraph[group[prev]].append(group[i])
                    groupIndegree[group[i]] += 1
        
        itemOrder = self.topologicalSort(itemGraph, itemIndegree)
        groupOrder = self.topologicalSort(groupGraph, groupIndegree)

        if not itemOrder or not groupOrder:
            return []
        
        orderedGroups = defaultdict(list)
        for item in itemOrder:
            orderedGroups[group[item]].append(item)
        
        answerList = []
        for groupIndex in groupOrder:
            answerList.extend(orderedGroups[groupIndex])
        return answerList

    def topologicalSort(self, graph, indegree):
        visited = []
        stack = []
        for i in range(len(indegree)):
            if indegree[i] == 0:
                stack.append(i)
        
        while stack:
            curr = stack.pop()
            visited.append(curr)

            for n in graph[curr]:
                indegree[n] -= 1
                if indegree[n] == 0:
                    stack.append(n)
        return visited if len(visited) == len(graph) else []