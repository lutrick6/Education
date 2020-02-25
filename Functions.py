# https://www.youtube.com/watch?v=9Os0o3wzS_I&list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU&index=8
# Functions
# Keep your code DRY (Don't Repeat Yourself)


# Create Standard function
def hello_func():
    pass


hello_func()

# Function will perform a print [ no need to call a print(function()) ]


def hello_func2():
    print('Hello Function!')


hello_func2()


# Return - Operate on data then pass it through the function
def hello_func3():
    return 'Hello Function'


print(hello_func3())  # Return allowed the function to be a string
print(len(hello_func3()))  # Now we can extract information from the function
print(hello_func3().upper())  # Now we can chain functions

# Arguments - This accepts a conditional value of the function(argument)


def new_function(greeting):
    # {} is a place holder that will be filled with an argument
    return '{} Friend.'.format(greeting)


print(new_function('Hi'))

# Additional Arguments - You can have an argument default to something


def new_function2(greeting, name='You'):
    return '{}, {}.'.format(greeting, name)


print(new_function2('Hi', name='Robert'))

# *Args & **KWArgs - this allows for any number of unknown arguments and keyword arguments


def student_info(*args, **kwargs):
    print(args)
    print(kwargs)


student_info('Math', 'Art', name='Robert', age=29)

# * & ** - This allows you to select how the values get unpacked into the funciton


def student_info2(*args, **kwargs):
    print(args)
    print(kwargs)


courses = ['Math', 'Art', 'CompSci']
info = {'name': 'Robert', 'age': 29}
student_info2(*courses, **info)


month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def is_leap(year):
    """Return True for Leap Years, False for non-Leap Years."""  # Function Explainer
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)    # Calculate Leap Year


def days_in_month(year, month):
    """Return number of days in that month in that year."""
    if not 1 <= month <= 12:    # if the month entered does not fall in the range of 1 - 12 returns invalid
        return 'Invalid Month'
    # if the month is equal to 2 and also falls on a leap year then return the leap year value: 29
    if month == 2 and is_leap(year):
        return 29
    return month_days[month]    # returns the list[value]


print(is_leap(2020))
print(days_in_month(2020, 2))
