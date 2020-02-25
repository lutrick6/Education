
with open('test.txt', 'r') as f:

    size_to_read = 100

    f_ccontents = f.read(size_to_read)

    print(f.tell())

    # while len(f_ccontents) > 0:
    #     print(f_ccontents, end='')
    #     f_ccontents = f.read(size_to_read)
