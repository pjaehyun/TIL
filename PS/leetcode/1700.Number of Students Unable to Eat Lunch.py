class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        while students:
            if sandwiches[0] not in students:
                return len(sandwiches)
            
            if students[0] == sandwiches[0]:
                students.pop(0)
                sandwiches.pop(0)
            else:
                temp = students.pop(0)
                students.append(temp)
        return 0
