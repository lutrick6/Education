# Python Object-Oriented Programming


class Employee:

    num_of_emps = 0
    raise_amount = 1.04

    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

        Employee.num_of_emps += 1


    def fullname(self):
        return '{} {}'.format(self.first, self.last)


    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)
    
    @classmethod
    def set_raise_amt(cls, amount):
        pass


emp_1 = Employee('Robert', 'Lutrick', 50000)
emp_2 = Employee('Solomon', 'Timothy-Mychael', 30000)


# Python OOP2: Class Variables
# Line 6,7 & 16 
# Employee.num_ofemps
# Employee.raise_amount
# Also see the init method for how it incriments the num_of_emps
# print(Employee.raise_amount)
# print(emp_1.raise_amount)
# print(emp_2.raise_amount)


# Python OOP3: Classmethods & staticmethods
