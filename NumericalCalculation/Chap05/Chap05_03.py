def counter(ss):
    small_counter = 0
    big_counter = 0
    num_counter = 0
    other_counter =  0
    for i in range(0, len(ss)):
        if ss[i] >'a' and  ss[i] < 'z':
            small_counter += 1
        elif ss[i] > 'A' and ss[i] < 'Z':
            big_counter += 1
        elif ss[i] > '0' and ss[i] < '9':
            num_counter += 1
        else:
            other_counter += 1
    return (big_counter,  small_counter, num_counter, other_counter)


if __name__ == '__main__':
    try:
        ss = "111,,,vvvvNNNN'"
        print(counter(ss))
    except e:
        print(e)
