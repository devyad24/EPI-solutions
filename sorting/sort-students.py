class Student(object):
    def __init__(self, name, grade_point_average):
        self.name = name
        self.grade_point_average = grade_point_average

    def __lt__(self, other):
        return self.name < other.name

students = [
            Student('A', 4.0), Student('C', 3.7), Student('D', 3.2), Student('B', 2.8)
        ]
students_sort_by_name = sorted(students)
print(f"students sorted by name: {[s.name for s in students]}")

#sort students in-place by grade_point_average
students.sort(key=lambda student: student.grade_point_average)
print(f"students sorted by name: {[s.grade_point_average for s in students]}")


