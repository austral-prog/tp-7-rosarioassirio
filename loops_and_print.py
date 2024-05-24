def enumerate_list(list):
    new_list = []
    index = 0
    for element in list:
        if element:
            new_list.append(f"{index}. {element}")
            index += 1
    return new_list

def enumerate_backwards(list):
    new_list = []
    index = 0
    for element in list:
        if element:
            new_list.append(f"{index}. {element[::-1]}")
            index += 1
    return new_list
