class Solution:
    def countStudents(self, students: list[int], sandwiches: list[int]) -> int:
        while students and sandwiches:
            if sandwiches[0] not in students:
                return len(students)
            
            if sandwiches[0] == students[0]:
                sandwiches.pop(0)
                students.pop(0)
            else:
                students.append(students.pop(0))
        
        return 0
        

s = Solution()

stu1 = [1,1,0,0]
sand1 = [0,1,0,1]

stu2 = [1,1,1,0,0,1]
sand2 = [1,0,0,0,1,1]

print(s.countStudents(stu1, sand1))
print(s.countStudents(stu2, sand2))