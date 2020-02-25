# def square(x):
#     return x * x

# def cube(x):
#     return x * x * x

# def my_map(func, arg_list):
#     result = []
#     for i in arg_list:
#         result.append(func(i))
#     return result

# squares = my_map(cube, [1, 2, 3, 4, 5])  # Note: cube function is not ran as cube() because the () is ran within the function.

# print(squares)



# examples
import os
import datetime as dt

def logger(msg):

    def log_message():
        print('Log: ', msg)
        var = str(dt.datetime.now()) + 'Log: ' + msg
        return var

    return log_message


log_hi = logger(os.logger.msg())
log_hi()

