def index_of_by_index (word, list, index):
  for i in range(index, len(list)):
        if list[i] == word:
            return i
    return -1

def index_of_empty(list):
    for i, index in enumerate(list):
        if index == "":
            return i
    return -1

def index_of(word, list):
    for i, index in enumerate(list):
        if index == word:
            return i
    return -1

def put(word, list):
    for i in range(len(list)):
        if list[i] == "":
            list[i] = word
            return i
    return -1

def remove(word, list):
    eliminate = 0
    for i in range(len(list)):
        if list[i] == word:
            list[i] = ""
            eliminate += 1
    return eliminate
