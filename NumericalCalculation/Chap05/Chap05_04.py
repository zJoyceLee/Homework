def foo():
    i=3
    return i

if __name__ == '__main__':
    try:
        i=1
        print(id(i))
        print(id(foo()))
    except e:
        print(e)
