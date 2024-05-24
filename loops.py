def index_of_by_index (word, list, index):
    if word in list [index:]:
        return list.index(word, index)
    else:
        return -1

def index_of_empty(list):
      if ("") in list:
        return list.index("")
    else:
        return -1

def index_of(word, list):
   if word in list:
        return list.index(word)
    else:
        return -1

def put(word, list):
     if "" in list:
        pos = list.index("")
        list[pos] = word
        return pos
    else:
        return -1

def remove(word, list):
    num = 0
    if word in list:
        for i in range(len(list)):
            if list[i] == word:
                list[i] = ""
                num += 1
        return num
    else:
        return 0
