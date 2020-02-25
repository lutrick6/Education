# https://www.youtube.com/watch?v=DZwmZ8Usvnk&list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU&index=6
# Conditions & Booleans - If, Else, and Elif


# Comparisons:
# Value:                =
# Equal:                ==
# Not Equal:            !=
# Greater Than:         >
# Less Than:            <
# Greater or Equal:     >=
# Less or Equal:        <=
# Object Identity:      is - id(a) == id(b)

language = 'Python'
if language == 'Python':
    print('Language is Python')
elif language == 'Java':
    print('Language is Java')
else:
    print('False was Condition')



# Booleans
# and
# or
# not

user = 'Admin'
logged_in = False

if user == 'Admin' or logged_in:
    print('Admin Page')
else:
    print('Bad Creds')



# False Values:
# False
# None
# Zero of any numeric type
# Any empty sequence. For example, ' ', (), [].
# Any empty mapping. For example, {}

condition = False
if condition:
    print('Evaluated True')
else:
    print('Evaluated False')
