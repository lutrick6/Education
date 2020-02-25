# https://www.youtube.com/watch?v=CqvZ3vGoGs0&list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU&index=9
# Import Modules and Exploring The Standard Library
# The Standard Library: os.__file__

import os
import calendar
import datetime
import math
import random
import sys
from testmodule import find_index, test
courses = ['History', 'Math', 'Physics', 'CompSci']

index = find_index(courses, 'Math')
print(index)
print(test)

# Print system paths to where python will import from
print(sys.path)
# Will add a new import path to check when searching
sys.path.append('/home/ilucid/Desktop')

random_course = random.choice(courses)
print(random_course)

rads = math.radians(90)
print(math.sin(rads))

today = datetime.date.today()
print(today)
print(calendar.isleap(2020))

print(os.getcwd())
print(os.__file__)  # Location of The Standard Library
