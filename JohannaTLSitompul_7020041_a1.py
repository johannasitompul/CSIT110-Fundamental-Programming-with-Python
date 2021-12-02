"""
Assignment 1

Name            : Johanna Then Lasmauli Sitompul
Student number  : 7020041
Subject code    : CSIT110
"""

name = 'Johanna Then Lasmauli Sitompul'
student_num = '7020041'
subject_code = 'CSIT110'


def question1():
    # print("Question 1. \n")
    int1 = int(input("Please enter the 1st integer: "))
    int2 = int(input("Please enter the 2nd integer: "))
    int3 = int(input("Please enter the 3rd integer: "))
    print("Display equation using string addition:", int1, "x", int2, "x", int3, "=", (int1 * int2 * int3))


def question2():
    # print("Question 2. \n")

    sub1_code = input("Enter the 1st subject code: ")
    sub1_title = input("Enter the 1st subject title: ")
    sub1_cp = int(input("Enter the 1st subject credit point: "))

    sub2_code = input("Enter the 2nd subject code: ")
    sub2_title = input("Enter the 2nd subject title: ")
    sub2_cp = int(input("Enter the 2nd subject credit point: "))

    print("Your chosen subjects: ")
    print("{} : {}".format(sub1_code, sub1_title))
    print("{} : {}".format(sub2_code, sub2_title))
    print("Total credit points: {}".format(sub1_cp + sub2_cp))


def question3():
    # print("Question 3. \n")

    adult_tix = int(input("How many adult tickets you want to order: "))
    child_over10 = int(input("How many children (3-12 years old) tickets: "))
    child_below10 = int(input("How many children (<3 years old) tickets: "))

    print(f"{'Type' : <20}{'Number of Tickets' : >17}{'Cost' : >15}")
    print(f"{'Adult' : <20}{adult_tix : >17}{'${:.2f}'.format(adult_tix * 39) : >15}")
    print(f"{'Children (3-12 y.o.)' : <20}{child_over10 : >17}{'${:.2f}'.format(child_over10 * 26.50) : >15}")
    print(f"{'Children (<3 y.o.)' : <20}{child_below10 : >17}{'free' : >15}")
    print(f"{'Total' : <20}{(adult_tix + child_over10 + child_below10) : >17}"
          f"{'${:.2f}'.format((adult_tix * 39) + (child_over10 * 26.50)) : >15}")


def question4():
    # print("Question 4. \n")

    assg = int(input("Enter your assignment mark: "))
    proj = int(input("Enter your project mark: "))
    exam = int(input("Enter your final exam mark: "))

    total = assg + proj + exam
    grade = " "

    if total < 60 or exam < 20:
        grade = "Fail"
    elif total < 75:
        grade = "C"
    elif total < 90:
        grade = "B"
    else:
        grade = "A"

    print("Your result:")
    print(f"{'Assignment:' : <22}{assg : >4}")
    print(f"{'Project:' : <22}{proj : >4}")
    print(f"{'Final exam:' : <22}{exam : >4}")
    print(f"{'Grade:' : <22}{grade : >4}")


def question5():
    # print("Question 5. \n")

    filename_list = []

    while True:
        str = input("Filename? ")

        while str.find("[") != -1:
            pos1 = str.find("[")
            pos2 = str.find("]") + 1
            str = str[:pos1] + str[pos2:]

        if str != "":
            filename_list.append(str)
        else:
            break

    for i in range(0, len(filename_list) - 1):
        print(filename_list[i], end=", ")

    print(filename_list[len(filename_list) - 1])


if __name__ == "__main__":
    print('Name:', name)
    print('Student No.:', student_num)
    print('Subject code:', subject_code)
    print('\nQUESTION 1\n')
    question1()
    print('\nQUESTION 2\n')
    question2()
    print('\nQUESTION 3\n')
    question3()
    print('\nQUESTION 4\n')
    question4()
    print('\nQUESTION 5\n')
    question5()
