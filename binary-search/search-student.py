import collections
import bisect

# search over non-primitive types
'''
given a list of students with name and their gpa in descending order, implement O(logn) search
'''
Student = collections.namedtuple('Student', ('grade_point_average','name'))

def comp_gpa(student):
    return (-student.grade_point_average, student.name)

def search_student(students, target, comp_gpa):
    i = bisect.bisect_left([comp_gpa(s) for s in students], comp_gpa(target))
    print(i)
    return 0 <= i <= len(students) and students[i] == target

students = {"alice": 3.9, "bob": 3.6, "jack": 3.4, "jill": 2.9}
stud = [Student(v,k) for k,v in students.items()]
target = Student(3.9, "alice")


print(search_student(stud, target, comp_gpa))


