# https://www.youtube.com/watch?v=6iF8Xb7Z3wQ&list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU&index=7
# Loops and Iterations - For/While Loops

# For Loop #
nums = [1, 2, 3, 4, 5]

# Basic for loop
for num in nums:
    print(num)

# Continue - Moves on to the next iteration of loop
for num in nums:
    if num ==3:
        print('Found it!')
        continue
    print(num)

# Break - Break out of the loop
for num in nums:
    if num ==3:
        print(num, 'Found it!')
        break
    print(num)

# Nested Loop - Will run through ever possible combination; 1.a, 1.b, 1.c, 2.a, 2.b, etc....
for num in nums:
    for letter in 'abc':
        print(num, letter)

# Range - Runs through a loop a certain number of times
for i in range(1, 11):
    print(i)



# While Loop #
x = 0

# Basic Loop
while x < 10:
    print(x)
    x += 1

# Break Loop
while x < 10:
    if x == 5:
        break
    print(x)
    x += 1

# Infinite Loop
while True:
    if x == 5:
        break
    print(x)
    x += 1
    