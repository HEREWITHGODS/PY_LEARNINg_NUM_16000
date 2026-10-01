student_grades = {"Anna":90, "Sergey":80, "Andrey":77}

def add_grade(name,grade):
    student_grades[name] = grade
    return student_grades

def avg_grades():
    return sum(student_grades.values())/len(student_grades)

def accept_grade(grade_level):
    for student, grade in student_grades.items():
        if grade>=grade_level:
            print(student)

print(add_grade("Masha",79))

print(avg_grades())

accept_grade(78)