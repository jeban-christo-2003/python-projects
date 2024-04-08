from typing import List

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        circular_count = students.count(0)  # Count of students preferring circular sandwiches
        square_count = students.count(1)    # Count of students preferring square sandwiches

        # Iterate through the sandwiches stack
        while sandwiches:
            if sandwiches[0] == students[0]:  # If the top sandwich matches the preference of the front student
                if sandwiches[0] == 0:
                    circular_count -= 1
                else:
                    square_count -= 1
                sandwiches.pop(0)  # The student takes the sandwich and leaves the queue
                students.pop(0)
            else:
                # If the top sandwich doesn't match the preference, move the student to the end of the queue
                students.append(students.pop(0))
                # If all students have been cycled through and none can eat the remaining sandwiches, break the loop
                if all(s != sandwiches[0] for s in students):
                    break

        # Return the count of students who couldn't eat
        return circular_count + square_count

# Test cases
solution = Solution()

# Test case 1
students1 = [1,1,0,0]
sandwiches1 = [0,1,0,1]
print("Test case 1:", solution.countStudents(students1, sandwiches1))  # Output should be 0

# Test case 2
students2 = [1,1,1,0,0,1]
sandwiches2 = [1,0,0,0,1,1]
print("Test case 2:", solution.countStudents(students2, sandwiches2))  # Output should be 3
