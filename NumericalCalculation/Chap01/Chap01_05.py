# python3 ./xx.py

def isallnum(ss):
    for i in ss:
        if i < '0' or i > '9':
            return False
    return True


if __name__=='__main__':
    try:
        ss = input("Please input a integer(>99): ")

        if isallnum(ss):
            num=eval(ss)

            if isinstance(num, int):
                if num > 99:
                    mytuple = divmod(num, 100)
                    print("int hund is %d"%mytuple[0])
                else:
                    print("The num is less than 100.")
        else:
            print('Input Error:: not number.')

    except (TypeError, NameError) as e:
        print(e)
