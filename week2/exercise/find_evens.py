def find_evens(li):
    evens_list = list()
    for i in li:
        if i % 2 != 0:
            evens_list.append(i)
    return evens_list
