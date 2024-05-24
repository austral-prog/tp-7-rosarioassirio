def index_of_by_index(x,y,z):
    index = -1
    if x in y[z::]:
        index = y[z::].index(x)
        index = index+z
    return index
index_of_by_index("Magenta",["Red", "Green", "White", "Black", "Pink", "Yellow", "Black", "Green", "Brown", "Red", "Black"], 1)


def index_of_empty(colors):
    for element in colors:
        if not element:
            return colors.index(element)
    return -1
index_of_empty(["Red", "Green", "", "", "Pink", "", "Black"])


def index_of(x,y):
    index = -1
    if x in y:
        index = y.index(x)
    return index
index_of("Black",["Red", "Green", "White", "Black", "Pink", "Yellow", "Black"])

def put(x, list):
    if index_of_empty(list) != -1:
        list[index_of_empty(list)] = x
        return list.index(x)
    else:
        return -1
put("Blue",["Red", "Green", "", "", "Pink", "", "Black"])


def remove(x, list):
    a = list.count(x)
    while x in list:
        list[list.index(x)] = ""
    return a
remove("Blue",["Red", "Green", "White", "Black", "Pink", "Yellow", "Black"])
