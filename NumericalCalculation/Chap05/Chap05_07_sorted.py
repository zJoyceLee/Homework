def mySorted(lst):
    for _ in lst:
        for i in range(0, len(lst) - 1):
            if lst[i] > lst[i + 1]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
    return lst

def mySorted_use_min(lst):
    ret = []
    length = len(lst)
    for _ in range(0, length):
        ret.append(min(lst))
        lst.remove(min(lst))
    return ret

if __name__ ==  '__main__':
    try:
        lst = [4, 5, 3, 1, 2]
        print(mySorted(lst))

        lst = [5, 4, 3, 2, 1]
        print(mySorted(lst))

        lst = [5, 4, 3, 2, 1]
        print(mySorted_use_min(lst))
    except e:
        print(e)
