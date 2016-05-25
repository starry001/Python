def flatten(nested):
    try:
        if isinstance(nested, str):
            raise TypeError
        for sublist in nested:
            for element in flatten(sublist):
                print('got:', element)
    except TypeError:
        print('here')
        yield nested


L = ['adddf', [1, 2, 3], 2, 4, [5, [6, [8, [9]], 'ddf'], 7]]
for enum in flatten(L):
    print(enum)
