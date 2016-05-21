# python3 ./Chap05_01.py

def demo(newitem, old_list = None):
    if old_list in None:
        old_list = []
    old_list.append(newitem)
    return old_list

if __name__ == '__main__':
    try:
        print(demo('5', [1, 2, 3, 4]))
        print(demo('aaa', ['a', 'b']))
        print(demo('a'))
        print(demo('b'))
    except (TypeError) as e:
        print(e)

# ~/Code/Python/NumericalCalculation/Chap05(branch:master*)
# » python Chap05_01.py                                                                                                                                                pi@raspberrypi
# Traceback (most recent call last):
#   File "Chap05_01.py", line 8, in <module>
#     print demo('5', [1, 2, 3, 4])
#   File "Chap05_01.py", line 2, in demo
#     if old_list in None:
# TypeError: argument of type 'NoneType' is not iterable

# ~/Code/Python/NumericalCalculation/Chap05(branch:master*)
# » python3 Chap05_01.py                                                                                                                                               pi@raspberrypi
# argument of type 'NoneType' is not iterable
