'''
LEGB
Local, Enclosing, Global, Built-in
'''

x = 'Global x'



def outer():


    # global x  # <<< this will affect all variables outside of the function: the Global x
    x = 'Enclosed x or nonlocal'



    def inner():
        # nonlocal x  # <<< this adjusts the one iteration above it: the Enclosed x
        x = 'Local x'
        print(x)



    inner()
    print(x)




outer()
print(x)
