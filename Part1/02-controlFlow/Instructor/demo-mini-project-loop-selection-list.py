
class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def assign_grade(self):
        if 90 <= self.score <= 100:
            return 'A'
        elif 80 <= self.score < 90:
            return 'B'
        elif 70 <= self.score < 80:
            return 'C'
        elif 60 <= self.score < 70:
            return 'D'
        else:
            return 'F'



# Create each student object and assign to individual variables
alice = Student("Alice", 85)
bob = Student("Bob", 59)
charlie = Student("Charlie", 92)
david = Student("David", 78)
eva = Student("Eva", 68)

# Collect all student objects into a list
students = [alice, bob, charlie, david, eva]

# Method 1
for student in students:
    print("Name ", student.name, " Score ", student.score)

# Method 2
for index in range(4):
    # Make sure student understands the meaning of students[index].name and
    # students[index].score
    print("Name ", students[index].name, " Score ", students[index].score)

# Method 3
# Improved version to replace 4 with the actual length of the list
length_of_list = len(students)
for index in range(length_of_list):
    # Make sure student understands the meaning of students[index].name and
    # students[index].score
    print("Name ", students[index].name, " Score ", students[index].score)
