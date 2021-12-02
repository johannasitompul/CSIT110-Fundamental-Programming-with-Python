'''
Assignment 2

Name            : Johanna Then Lasmauli Sitompul
Student number  : 7020041
Subject code    : CSIT110
'''

name = 'Johanna Then Lasmauli Sitompul'
student_num = '7020041'  # Student number
subject_code = 'CSIT110'  # CSIT110 or SP420

# ===========Insert your solution to Question 1 here =================#

channels = {
    "Sports Group Pack" : 21.40,
    "Documentaries Pack" : 15.32,
    "Fox Movie Pack" : 17.12,
    "HBO Pack" : 13.98,
    "Cinema World" : 9.56,
    "Celestial Movies" : 8.56
}

'''
def display_channels():
    print("Channels available for subscription (price/mth)")
    for i in channels:
        print(f"{i : <35} { '${:.2f}'.format(channels[i]) : >11}")
    print(" ")
'''

def get_subscription():

    def display_channels():
        print("Channels available for subscription (price/mth)")
        for i in channels:
            print(f"{i : <35} {'${:.2f}'.format(channels[i]) : >11}")
        print(" ")

    display_channels()
    total = 0
    subbed = []

    for i in channels:
        user_input = input("Subscribe to " + i + "? (Y/N): ")
        if user_input.upper() == "Y":
            subbed.append(i)
            total = total + channels[i]

    print("\nYour selection:")
    if len(subbed) != 0:
        for i in range(0, len(subbed)):
            print(" -", subbed[i], "${:.2f}".format(channels.get(subbed[i])))
    else:
        print(" - None")

    print("\nTotal cost ${:.2f}".format(total))

#get_subscription()

# ======================= End of Question 1 ==========================#


# ===========Insert your solution to Question 2 here =================#

'''
def multiply(list):
    result = 1
    for i in list:
        result = result * i
    return result

def to_str(list):
    string = str(list[0])
    for i in range(1, len(list)):
        string = string + " x " + str(list[i])
    return string
'''

def generate_qns_from_list(list):

    def multiply(list):
        result = 1
        for i in list:
            result = result * i
        return result

    def to_str(list):
        string = str(list[0])
        for i in range(1, len(list)):
            string = string + " x " + str(list[i])
        return string

    output_list = []
    for i in range(0, len(list)):
        if len(list[i]) > 1:
            multi = {
                'qns': to_str(list[i]),
                'ans': multiply(list[i])
            }
            output_list.append(multi)
    return output_list

#input_list = [[1,3,3], [2,5,-1], [3,2], [4,5,3], [0,23], [1,2,3,4], [1]]
#print(generate_qns_from_list(input_list))

# ======================= End of Question 2 ==========================#


# ===========Insert your solution to Question 3 here =================#

class ShoppingCart:
    server_url = "128.123.123.0"

    def __init__(self, account_id):
        self.account_id = account_id
        self.cart = {}

    def add_item_to_cart(self, name, qty):
        if len(self.cart) > 0:
            for i in self.cart:
                if name == i:
                    self.cart[i] += qty
                    break
                else:
                    self.cart[name] = qty
                    break
        else:
            self.cart[name] = qty

    def remove_item_from_cart(self, name, qty):
        for i in self.cart:
            if name == i:
                self.cart[i] -= qty
                if self.cart[i] == 0:
                    del self.cart[i]
                    break

    def count_items(self):
        total = 0
        for i in self.cart:
            total += self.cart[i]
        return total

    def get_url(self):
        return self.server_url

    def empty_cart(self):
        self.cart.clear()

'''
newCart = ShoppingCart('123456')
print(newCart.account_id)
newCart.add_item_to_cart('fruit juice', 2)
newCart.add_item_to_cart('tissue box', 4)
newCart.add_item_to_cart('ice cream', 3)
newCart.remove_item_from_cart('tissue box',1)
newCart.remove_item_from_cart('fruit juice',2)
print(newCart.cart)
print(newCart.count_items())
print(newCart.get_url())
newCart.empty_cart()
print(newCart.count_items())
'''

# ======================= End of Question 3 ==========================#


# ===========Insert your solution to Question 4 here =================#

class Student:
    def __init__(self, dict_obj):
        self.name = dict_obj['name']
        self.results = dict_obj['results']
    def get_weighted_results(self, weights_dict):
        result = 0
        for key in weights_dict:
            temp = weights_dict[key] * self.results[key]
            result += temp
        return result
    def display(self):
        print(self.name, self.results)


def dict_to_class_obj(dict_list):
    class_list = []
    for i in range(0, len(dict_list)):
        temp = Student(dict_list[i])
        class_list.append(temp)
    return class_list

'''
stud1 = {
    "name": "Fus Ro Dah",
    "results": {
        "assignment_1": 10,
        "assignment_2": 10,
        "examination_1": 10,
    }
}

dictList = [
    {
        "name": "Fus Ro Dah",
        "results": {
            "assignment_1": 10,
            "assignment_2": 10,
            "examination_1": 10,
        },
    },
    {
        "name": "Foo Barry",
        "results": {
            "assignment_1": 1,
            "assignment_2": 2,
            "examination_1": 3,
        },
    },
]

weights = {"assignment_1": 1.0, "examination_1": 9.0}

classList = dict_to_class_obj(dictList)

for i in range(0, len(classList)):
    classList[i].display()
    print(classList[i].get_weighted_results(weights))
'''

# ======================= End of Question 4 ==========================#

def main():
    print("hi")
    ## use this space to test your functions and class
    ## code in this space will not be run during testing

if __name__ == "__main__":
    main()
