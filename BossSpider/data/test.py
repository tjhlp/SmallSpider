def merge_letter(letter_dict):
    """

    :param letter_dict:
    :return:返回小写字母组成的数字
    """
    new_dict = {}
    for key, value in letter_dict.items():
        print(key)
        print(value)
        if key.lower() in new_dict:
            new_dict[key.lower()] += value
        else:
            new_dict[key.lower()] = value
    return new_dict


a = {'a': 1, 'b': 2, 'A': 1, 'B': 3}
print(merge_letter(a))
