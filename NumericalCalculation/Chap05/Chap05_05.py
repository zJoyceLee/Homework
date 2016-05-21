import math

def is_int(ss):
    for i in range(0, len(ss)):
        if ss[i] < '0' or ss[i] > '9':
            return False
    return True


def to_lst(ss):
    myIntList = []
    lst = ss.split()
    for i in range(0, len(lst)):
        if is_int(lst[i]):
            myIntList.append(int(lst[i]))
#             print('%d: 1'%int(lst[i]))
#         else:
#             print('%s: -1'%lst[i])
    return myIntList


if __name__ == '__main__':
    try:
        # ss = raw_input('Please enter some integer: ')
        # print(max(int(x) for x in ss.split(' ')))
        # print(sum(int(x) for x in ss.split(' ')))
        ss = '2 123 3.4 , ; a p '
        intLst = to_lst(ss)
        # int list
        print(intLst)

        maxInt = max(intLst)
        print('Max int is: %d'%maxInt)

        mysum = sum(intLst)
        print('Sum is: %d'%mysum)

    except e:
        print(e)
