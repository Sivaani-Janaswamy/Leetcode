class Solution(object):
    def countStudents(self, students, sandwiches):
        unableToEat = 0
        
        while students and unableToEat < len(students):
            currentStudent = students.pop(0)

            if currentStudent == sandwiches[0]:
                sandwiches.pop(0)
                unableToEat = 0        
            else:
                students.append(currentStudent)
                unableToEat += 1      

        return len(students)
