class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

students = [Student("Omar", 0.78), Student("Bayezid", 0.80), Student("Abu Isa", 0.70), Student("Ashraf", 0.90), Student("Mostaq", 0.70), Student("Tutul", 0.65), Student("Osman", 0.66)]
student_result = []
#for student in students:
    # if student.score >= 0.7:
    #     student_result.append(f"{student.name} Passed")
    # else:
    #     student_result.append(f"{student.name} Failed")

[student_result.append(f"{student.name} Passed") if student.score >= 0.7 else student_result.append(f"{student.name} Failed") for student in students]

print(student_result)

numbers = [1,2,3,4,5]

print(list(map(lambda num: num*2, numbers)))

even = print(list(filter(lambda number: number % 2 == 0,numbers)))