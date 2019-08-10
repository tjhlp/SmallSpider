data_dict = {'a': 1, 'b': 2,'c':3}


def func(a, b, c):
    print(a)
    print(b)
    print(c)


func(**data_dict)
