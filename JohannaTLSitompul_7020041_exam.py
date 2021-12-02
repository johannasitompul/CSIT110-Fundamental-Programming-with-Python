""" Examination

    student_name = 'Johanna Then Lasmauli Sitompul'
    student_uow_id = '7020041'
    course_code = 'CSIT110'

"""
student_name = 'Johanna Then Lasmauli Sitompul'
student_uow_id = '7020041'
course_code = 'CSIT110'

#===========================================#
#############################################
############# All the best! #################
#############################################
#===========================================#

#===========================================#
#==== Insert solution to question 1 here====#

def question_1a(list1, list2):
    list1.extend(list2)
    return list1

def question_1b(list, item):
    if item in list:
        pos = list.index(item)
    else:
        return -1
    return pos

def question_1c(x, N):
    num_list = []
    for i in range (0, N):
        num_list.append(x)
    return num_list

def question_1d(list, num):
    result = list.count(num)
    return result

def dot_product(list1, list2):
    result = 0
    for i in range(0, len(list1)):
        temp = list1[i] * list2[i]
        result = result + temp
    return result

def root_mean_square(list):
    import math
    sum = 0
    for i in range (0, len(list)):
        temp = list[i] ** 2
        sum = sum + temp
    mean = sum/len(list)
    result = math.sqrt(mean)
    return result

def list_to_dict(list):
    output_dict = {}
    for i in range (0, len(list)):
        mini_list = list[i]
        output_dict[mini_list[0]] = mini_list[1]
    return output_dict

def question_1h(string):
    raise ValueError(string)

def question_1i():
    output = ""
    user_input = float(input("Enter size: "))
    if user_input < 8:
        output = "XS"
    if 8 <= user_input < 10:
        output = "XS"
    if 10 <= user_input <= 14:
        output = "M"
    if user_input > 14:
        output = "L"
    return output

def question_1j(N):
    import random
    total = 1
    num_list = []

    for i in range (0, N):
        num = random.randint(0,100)
        total = total * num
        num_list.append(num)

    def to_str(list):
        string = str(list[0])
        for i in range(1, len(list)):
            string = string + " x " + str(list[i])
        return string

    output = {
        'qns': to_str(num_list),
        'ans': total
    }

    return output

#===========================================#
#==== Insert solution to question 2 here====#

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    @classmethod
    def from_dict(cls, dict):
        return cls(dict["name"], dict["price"])

#===========================================#
#===============Question 3 =================#

# Do not modify, do not remove
class NoGradesError(Exception):
    pass

# Do not modify, do not remove
class Student():
    def __init__(self, name = "", grades=None):
        self.name: str = name  # name is of str type.
        self.__grades = grades  # grades will be a list of floats

    def get_grades(self):  #This function will return a list of floats
        if self.__grades == None:
            raise NoGradesError()
        return self.__grades

#===========================================#
#==== Insert solution to question 3 here====#

def get_class_statistics(list):
    pass_count = 0
    fail_count = 0
    for i in range(0, len(list)):
        try:
            total = sum(list[i].get_grades())
            if total >= 50:
                pass_count += 1
            if total < 50:
                fail_count += 1
        except:
            pass

    invalid_count = len(list) - pass_count - fail_count

    output_dict = {
        'pass_count': pass_count,
        'fail_count': fail_count,
        'invalid_count': invalid_count
    }

    return output_dict

#===========================================#
#==== Insert solution to question 4 here====#

class Staff:
    def __init__(self, name, staff_num, salary, staff_benefits=True):
        self.name = name
        self.staff_num = staff_num
        self.salary = salary
        self.staff_benefits = staff_benefits

    def get_paycheck(self):
        return self.salary


class ContractStaff(Staff):
    def __init__(self, name, staff_num, hourly_rate, hours_worked=0):
        super().__init__(name, staff_num, None, False)
        self.hourly_rate = hourly_rate
        self.hours_worked = 0

    def add_hours_worked(self, hours_worked):
        self.hours_worked = hours_worked

    def get_paycheck(self):
        result = self.hourly_rate * self.hours_worked
        return result

#=============End of question 4 ============#


#===========================================#
#############################################
############# Almost done! ##################
#############################################
#===========================================#


#===============Question 5 =================#

# do not modify or remove
class HighSchoolStudent():
    def __init__(self, name, grades):
        # READ ME!
        # the parameter, name, will be of str type.
        # the parameter, grades, will be a dictionary with string as keys and float as values.
        #         e.g. {"qwe": 1.1, "asd":5.9}
        self.__name = name
        self.__grades = grades

    def get_name(self):  # The function will return a string
        return self.__name

    def get_grades(self):  #The function returns a dictionary with string as keys and float as values.
        return self.__grades

#==== Insert solution to question 5 here====#

def get_student_report(student):
    try:
        name = student.get_name()
        total_width = 0

        def display_dict(dict):
            sub_width = 0
            grade_width = 0
            total_grade = 0

            for key in dict:
                if len(key) > sub_width:
                    sub_width = len(key)
                string = str(dict[key])
                if len(string) > grade_width:
                    grade_width = len(string)

            total_width = sub_width + grade_width

            string = ""

            for key in dict:
                string += f"{key : >{sub_width}}: {'{:.1f}'.format(dict[key]) : >{grade_width}}\n"
                total_grade += dict[key]

            dashes = "-" * (total_width+2)
            total_grade_string = f"{'Total Grade' : >{sub_width}}: {'{:.1f}'.format(total_grade) : >{grade_width}}\n"

            string = string + dashes + "\n" + total_grade_string
            return string

        subject_grade = display_dict(student.get_grades())

        output = name + "\n" + subject_grade
        return output
    except:
        pass

def main():
    pass  # comment this line if you want to test your code here.
    # uncomment pass if you chose to comment all your testcode before submission.


if __name__ == '__main__':
    main()