def remove_repeater(lst):
    ret = []
    for i in range(0, len(lst)):
        if lst[i] not in ret:
            ret.append(lst[i])
    return ret

def list2string(lst):
    ret = ''
    for i in range(0, len(lst) - 1):
        ret += lst[i] + ' '
    ret += lst[-1]
    return ret

ss = "This is is a desk."
print(ss)
lst = ss.split()
print(lst)

lst = remove_repeater(lst)
print(lst)

ss = list2string(lst)
print(ss)
