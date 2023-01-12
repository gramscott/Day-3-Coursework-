def return_10():
    return 10


def add(num1, num2):
    return num1 + num2


def subtract(num10, num5):
    return num10 - num5


def multiply(times4, times2):
    return times4 * times2

def divide(divide10, divide2):
    return divide10 / divide2

def length_of_string(test_string="A string of length 21"):
    return len(test_string)

def join_string(string_1 = "Mary had a little lamb, ",
      string_2 = "its fleece was white as snow"):
      return string_1 + string_2

def add_string_as_number(num1, num2):
    return int(num1) + int(num2)

months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    
def number_to_full_month_name(month):
    return months[month-1]

def number_to_short_month_name(month):
    return months[month-1][:3]