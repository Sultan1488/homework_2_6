def my_func(dict_1):
    if type(dict_1) == dict:
        for x in dict_1:
            if dict_1[x] == []:
                empty_list = {f'{x}\'s rating': 0 for x in dict_1}
                return empty_list
            else:
                final_dict = {
                    f'{x}\'s rating':
                        sum(dict_1[x]) / len(dict_1[x])
                        for x in dict_1
                    }
                return final_dict
    else:
        raise ValueError
