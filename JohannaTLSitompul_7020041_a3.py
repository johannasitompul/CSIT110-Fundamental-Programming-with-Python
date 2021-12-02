""" Template for Assignment 3
    Use this template for submission.
    - This template includes an example function.
    - Note that the template uses 4 space for indenation
      which you may choose to replace as tabs

    student_name = 'Johanna Then Lasmauli Sitompul'
    student_uow_id = '7020041'
    course_code = 'CSIT110'

"""
student_name = 'Johanna Then Lasmauli Sitompul'
student_uow_id = '7020041'
course_code = 'CSIT110'

"""Insert your solution between these lines"""


# QUESTION 1
def myClass_get_int_unit_test(inputClass):
    try:
        obj = inputClass()
        obj.get_integer()
    except AttributeError as e:
        return 'A'
    except ValueError as e:
        return 'V'
    except:
        return 'O'

# QUESTION 2
def compute_unit_prices(price_qty_dict, name_list):
    output_dict = {}

    try:
        def get_unit_price(price_qty_list):
            try:
                price = price_qty_list[0]
                qty = price_qty_list[1]
                unit_price = price / qty
                return unit_price
            except ZeroDivisionError as e:
                return -1

        for i in range (0, len(name_list)):
            try:
                name = name_list[i]
                price_qty_list = price_qty_dict.get(name)
                unit_price = get_unit_price(price_qty_list)
                output_dict[name] = unit_price
            except TypeError as e:
                output_dict[name] = None

        return output_dict

    except:
        output_dict = {}
        return output_dict

'''
dict = {
    "vinegar": [120.0, 100],
    "ketchup": [950, 1000],
    "apples": [850,1100],
    "oranges": [1050, 0],
}

list = ["ketchup","oranges","pear"]

print(compute_unit_prices(dict,list))
'''

# QUESTION 3
class AssessmentNotFoundError(Exception):
    def __init__(self, assess_name, std_name):
        self.assess_name = assess_name
        self.std_name = std_name

    def __str__(self):
        return "{} results cannot be found in {}'s results".format(self.assess_name, self.std_name)

class Student:
    def __init__(self, dict_obj):
        self.name = dict_obj['name']
        self.results = dict_obj['results']

    def get_weighted_result(self, weights_dict):
        result = 0
#        try:
        for key in weights_dict:
            if key not in self.results:
                raise AssessmentNotFoundError(key, self.name)
            result += weights_dict[key] * self.results[key]
        return result
#        except AssessmentNotFoundError as e:
#            print(e)

    def display(self):
        print(self.name, self.results)

'''
stud1_dict = {
    "name": "Fus Ro Dah",
    "results": {
        "assignment_1": 10,
        "assignment_2": 10,
        "examination_1": 10,
    }
}

stud1 = Student(stud1_dict)
weights = {"assignment_1": 1.0, "examination_1": 9.0}
stud1.display()
print(stud1.get_weighted_result(weights))
'''

# QUESTION 4
class InvalidDepthError(Exception):
    def __str__(self):
        return 'Invalid Depth'

class WaterBody:
    RHO = 997
    G = 9.81

    def __init__(self, a_number):
        self.volume = a_number

    @staticmethod
    def get_hydrostatic_pressure(a_float):
        if a_float < 0:
            raise InvalidDepthError
        result = 997 * 9.81 * a_float
        return result

    def get_water_mass(self):
        result = self.RHO * self.volume
        return result

    @staticmethod
    def is_large(a_number):
        if a_number > 100:
            return True
        else:
            return False

    @staticmethod
    def is_medium(a_number):
        if 50 <= a_number <= 100:
            return True
        else:
            return False

    @staticmethod
    def is_small(a_number):
        if a_number < 50:
            return True
        else:
            return False

    @classmethod
    def spawn(cls):
        import random
        random_number = random.randint(0,1000)
        return cls(random_number)


#x = WaterBody(10)
#print(x.get_hydrostatic_pressure(2))

'''
pool = WaterBody(10)
print(pool.get_hydrostatic_pressure(1)) # prints 9780.57
print(pool.get_water_mass()) # prints 9970

try:
    pool.get_hydrostatic_pressure(-1)
except Exception as e:
    print(e) # prints Invalid Depth
'''

# QUESTION 5
class SingaporeNumbers:
    def __init__(self):
        pass

    @staticmethod
    def car_plate_checksum(string):
        fix_num = [9, 4, 5, 4, 3, 2]
        car_num = [0, 0, 0, 0, 0, 0]
        checksum_alpha = ['A','Z','Y','X','U','T','S','R','P','M','L','K','J','H','G','E','D','C','B']

        def to_digit(string):
            result = ord(string.lower()) - 96
            return result

        def multiply_and_sum(list1, list2):
            result = 0
            for i in range(0, len(list1)):
                temp = list1[i] * list2[i]
                result = result + temp
            return result

        for i in string:
            if i.isdigit():
                pos = string.find(i)
                break

        num_of_digits = len(string) - pos
        num_of_alpha = pos

        if num_of_alpha == 1:
            car_num[1] = to_digit(string[0])
        if num_of_alpha == 2:
            car_num[0] = to_digit(string[0])
            car_num[1] = to_digit(string[1])
        if num_of_alpha == 3:
            car_num[0] = to_digit(string[1])
            car_num[1] = to_digit(string[2])

        for i in range(1, num_of_digits + 1):
            car_num[-i] = int(string[len(string) - i])

        remainder = multiply_and_sum(fix_num, car_num) % 19
        checksum = checksum_alpha[remainder]
        return checksum

    @staticmethod
    def magic_num_checksum(string):
        fix_num = [2, 7, 6, 5, 4, 3, 2]
        checksum_alpha = ['J','Z','I','H','G','F','E','D','C','B','A']
        total = 0
        for i in range(0,7):
            temp = int(string[i]) * fix_num[i]
            total = total + temp
        remainder = total % 11
        checksum = checksum_alpha[remainder]
        return checksum

'''
if num_of_digits == 1:
    car_num[5] = string[pos]
if num_of_digits == 2:
    car_num[4] = string[pos]
    car_num[5] = string[pos+1]
if num_of_digits == 3:
    car_num[3] = string[pos]
    car_num[4] = string[pos+1]
    car_num[5] = string[pos+2]
if num_of_digits == 4:
    car_num[2] = string[pos]
    car_num[3] = string[pos+1]
    car_num[4] = string[pos+2]
    car_num[5] = string[pos+3]

x = SingaporeNumbers.car_plate_checksum('E23')
y = SingaporeNumbers.magic_num_checksum('1234567')
print(y)
'''


"""Insert your solution between these lines"""

def myClass_demo_unit_test(inputClass):
    """ This example takes in a class definition as input,
        then instantiates a class object and test its method
        in a try except system.
    """
    try:
        obj = inputClass()
        obj.demo()
    except ValueError as e:
        print('A ValueError was raised because ' + str(e))


def example():
    # A class with one method
    class MyClass():
        def __init__(self):
            pass
        def demo(self):
            raise ValueError('Wrong input given!')

    # test the demo method
    myClass_demo_unit_test(MyClass)
    # myClass_get_int_unit_test(MyClass)


def main():
    """an example function that creates a class and feeds into
    the class into the myClass_demo_unit_test for testing
    You are free to create your own test subjects that raise
    errors to test your code here."""
    example()


if __name__ == '__main__':
    main()