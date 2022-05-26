#TASK1
import random
class CFGStudent:

    def __init__(self,name, surname, age, email, student_id):
        self.name = name
        self.surname = surname
        self.age = age
        self.email = email
        self.student_id = student_id

        self.course_grades = {
            'Ana': {'HW': 79, 'Theory1': 68, 'Theory2': 79},
            'Mia': {'HW': 61, 'Theory1': 100, 'Theory2': 96, },
            'Sara': {'HW': 88, 'Theory1': 90, 'Theory2': 98, }
        }

    @staticmethod
    def generate_id():
        student_id = random.randint(1000,10000)
        print(str(student_id))

    def get_id(self):
        print(self.student_id)

    def get_fullname(self):
        full_name = [self.name, self.surname]
        print(full_name)


class NanoStudent(CFGStudent):
     def __init__(self, specialization, course_grades, name, surname, age, email, student_id):
        super().__init__(name, surname, age, email, student_id)
        self.specialization = specialization
        self.course_grades = course_grades


#     @staticmethod
    def generate_id(self):
        self.student_id = random.randint(1000,10000)
        print('f NANO {self.student_id} ')
#
#
    def add_new_grade(self,):
        course_grade = {}
        new_assignment = input('What is the assignment you want to add?')
        new_assignment_grade  = input('What was the score for this assignment?')
        self.specializarion[self.name].update(new_assignment = new_assignment)
        self.course_grades[self.name].update( new_assignment_grade = float(new_assignment_grade))
        print(self.specialization[self.name])
        print(self.course_grades[self.name)

    def get_course_grades(self):
        print(self.course_grades)

s = CFGStudent('Anna', 'Smith', 18, 'anna@mail.com')
print(s.get_fullname())
# returns 'Anna Smith'
print(s.student_id)

cfg_s = NanoStudent('Software', 'Mia','Papandopulu', 20, 'mia@mail.com')
print(cfg_s.get_fullname())
# returns 'Mia Papandopulu'
print(cfg_s.get_id())
# returns 'NANO6180' or some other random number

cfg_s.add_new_grade('theory', 95)
cfg_s.add_new_grade('project', 78)
print(cfg_s.get_course_grades())
# returns {'theory': 95, 'project': 78}

#TASK2
def fib_sum_evn(limit):
    if (limit < 2):
        return 0


    fib_1 = 0
    fib_2 = 2
    fib_sum = fib_1 + fib_2


    while (fib_2 <= limit):


        fib_3 = 4 * fib_2 + fib_1


        if (fib_3 > limit):
            break


        fib_1 = fib_2
        fib_2 = fib_3
        fib_sum = fib_sum + fib_3

    return fib_sum

limit = 10
print(fib_sum_evn(limit))

#TASK3
def is_valid_subsequence(array, sequence):
	i = 0
	for num in array:
		if i == len(sequence):
			break
		if sequence[i] == num:
			i += 1
	return i == len(sequence)

array = [5,1,22,25,6,-1,8,10]
sequence = [1,6,-1,-2]
print(is_valid_subsequence(array, sequence))
#output False

# 2
# array2 = [5,1,22,25,6,-1,8,10]
# sequence2 = [1,6,-1, 10]
#
# print(is_valid_subsequence(array2, sequence2))  # TRUE
#
#
# array3 = [5,1,22,25,6,-1,8,10]
# sequence3 = [25]
#
# print(is_valid_subsequence(array3, sequence3))  # TRUE
