# List - Lists are mutable: the values can be modified (removed, amended, inserted, etc...)
courses = [
    'history',
    'math',
    'physics',
    'compSci'
]

courses_2 = [
    'Art',
    'Design',
    'Theatre'
]

nums = [
    '1',
    '3',
    '5',
    '2',
    '4'
]

# list[-1] - Last Value in the list
print(courses[-1])

# list.append('value') - adds a value to the list
courses.append('art')

# list.insert(location, 'value') - inserts value into a location of the list
courses.insert(0, "Art")

# list.extend(list2) - Adds the values in another list2 to the list
courses.extend(courses_2)

# list.remove('value') - Removes a value from the list
courses.remove('math')

# list.pop() - Removes the last value in the list
courses.pop()

# list.reverse() - Reverses values in the list
courses.reverse()

# list.sort() - Sorts the list; sort(argument) - sort(reverse=True)
courses.sort()

# sorted(list) - Sorts the list with out altering the orginal
sorted_courses = sorted(courses)

# min(list), max(list), sum(list)  - minimum value, maximum value, and sum value of the list
print(max(nums))

# print(list.index('value')) - prints the lists' index-number of the given value
print(courses.index('math'))

# for i in enumerate(list) - enumerate function can be applied to the list to add the index-number to the value
for course in enumerate(courses):
    print(courses)

# Enumerate can start at 1 or accept additional arguments
for index, course in enumerate(courses, start=1):
    print(index, course)

# variable = 'seperator'.join(list) - will join the values of the list and then use the seperator to part them
course_str = ' - '.join(courses)

# variable = variable.split('seperator') - split will split everythig up based on the seperator. This returns the string to a list
new_list = course_str.split(' - ')

#======================================================================================================


# Tupl - Tupl are immutable: the values cannot be modified
school = (
    'Harvard',
    'Princeton',
    'Oxford'
)


#======================================================================================================


# Sets - 
buildings = {'north', 'south', 'east', 'west'}
morebuildings = {'north', 'south', 'northeast', 'northwest', 'southeast', 'southwest'}

# set.intersection(set2) - Intersection will display common values  
print(buildings.intersection(morebuildings))

# set.difference(set2) - Difference will display "set" values not lsted in "set2"
print(buildings.difference(morebuildings))

# set.union(set2) - Union will display all unique values
print(buildings.union(morebuildings))


#======================================================================================================


# Empty Lists
empty_list = []
empty_list = list()

# Empty Tuples
empty_tuple = ()
empty_tuple = tuple()

# Empty Sets
empty_set = {} # THIS ISN'T RIGHT! ITS A DICT
empty_set = set()