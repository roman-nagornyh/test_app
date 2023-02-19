
def removing_duplicates(name):
    symbol_list = list(name)
    for search_symbol in symbol_list:
        count_copy = 0
        for index, symbol in enumerate(symbol_list):
            if symbol == search_symbol:
                count_copy += 1
            if count_copy > 1:
                count_copy = 1
                del symbol_list[index]

    return "".join(symbol_list)


def file_name():
    test_list = input('Введите имена файлов через пробел:').split(' ')
    max_len = len(max(test_list, key=len))
    for index, name in enumerate(test_list):
        name = removing_duplicates(name)
        name_len = len(name)
        if name_len < max_len:
            name += '_'*(max_len-name_len)
        with open('files/'+name+'.txt', 'w+') as openfile:
            pass
        openfile.close()


