# https://www.youtube.com/watch?v=daefaLgNkw0&list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU&index=5
# Dictionaries


Student = {
    'name': 'John',
    'age': 25,
    'courses': 
    [
        'math', 'compsci'
    ]
}

# dictionary.get('value', 'default return') - Get will test for a value, if value is not found will display a default return
#Student.get('phone', 'Not Found')

# dictionary.update({'value': 'newValue','etc':'newEtc'}) - Update the dictionary's values
#Student.update({'name': 'Robert', 'phone': '479-6515', 'age': 29})

# del dictionary['value'] - Delete a value with the dictionary
#del Student['age']

# variable = dictionary.pop('value') - Pop out a value with out deleting it
#age = Student.pop('age')

# print(len(dictionary)) - print the number of items in the dictionary
#print(len(Student))

# print(dictionary.item()) - 'keys': 'values'
#Student.keys()
#Student.values()
# print(dictionary.items()) - (''keys': 'values')
#Student.items()

test = Student.__contains__('age')
if test == True:
    print ('this worked')

# for key, value in Student.items():
#     print(key, value)