nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# my_list = []
# for n in nums:
# my_list.append(n)
# print(my_list)
#!!!~~~Comprehension~~~!!!#
# my_list = [n for n in nums]
# print(my_list)
#
#
# my_list = []
# for n in nums:
# my_list.append(n*n)
# print(my_list)
#!!!~~~Comprehension~~~!!!#
# my_list = [n*n for n in nums]
# print(my_list)


# my_list = []
# for n in nums:
# if n % 2 == 0:
# my_list.append(n)
# print(my_list)
#!!!~~~Comprehension~~~!!!#
# my_list = [n for n in nums if n % 2 == 0]
# print(my_list)


# my_list = []
# for letter in 'abcd':
# for num in range(4):
# my_list.append((letter, num))
# print(my_list)
#!!!~~~Comprehension~~~!!!#
# my_list = [(letter, num) for letter in 'abcd' for num in range(4)]
# print(my_list)

names = ['Bruce', 'Clark', 'Peter', 'Logan', 'Wade']
heros = ['Batman', 'Superman', 'Spiderman', 'Wolverine', 'Deadpool']
# something = list(zip(names, heros))
# print(something)

# my_dict = {}
# for name, hero in zip(names, heros):
# my_dict[name] = hero
# print(my_dict)
#!!!~~~Comprehension~~~!!!#
# my_dict = {name: hero for name, hero in zip(names, heros)}
# print(my_dict)
# if you want to remove 1 item from the list you can easily add: if name != 'Peter'
# my_dict = {name: hero for name, hero in zip(names, heros) if name != 'Peter'}
# print(my_dict)


# nums = [1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 5, 5, 6, 7, 7, 8]
# my_set = set()
# for n in nums:
# my_set.add(n)
# print(my_set)
#!!!~~~Comprehension~~~!!!#
# my_set = {n for n in nums}


# Generator Experessions
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# def gen_func(nums):
# for n in nums:
# yield n*n
#
# my_gen = gen_func(nums)
#!!!~~~Comprehension~~~!!!#
my_gen = (n*n for n in nums)

for i in my_gen:
    print(i)
