def list2string(lst):
    ret = ''
    for i in range(0, len(lst) - 1):
        ret += lst[i] + ' '
    ret += lst[-1]
    return ret

# ss = 'eee eee uau aehc nhuuet  ituhine thc thnh the hello world oh.'
ss = raw_input("Please enter some charactors: ")
lst = ss.split()
for word in lst:
    if len(word) == 3 and word[2] != '.':
        print(word)
