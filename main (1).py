class Student:
    def __init__(self, name, roll_number, cgpa):
        self.name = name
        self.roll_number = roll_number
        self.cgpa = cgpa

    def __repr__(self):
        return f"Student(name='{self.name}', roll_number='{self.roll_number}', cgpa={self.cgpa})"


def sort_students(student_list):
    """
    Sort a list of student objects based on their CGPA in descending order.

    Parameters:
    student_list (list): List of student objects.

    Returns:
    list: Sorted list of student objects based on CGPA in descending order.
    """
    sorted_students = sorted(student_list, key=lambda student: student.cgpa, reverse=True)
    return sorted_students


# Example usage
students = [
    Student("Arun", "001", 3.8),
    Student("Balaji", "002", 3.5),
    Student("Mari", "003", 3.9),
    Student("Sam", "004", 3.7)
]

print("Original student list:")
for student in students:
    print(student)

sorted_students = sort_students(students)

print("\nSorted student list based on CGPA in descending order:")
for student in sorted_students:
    print(student)