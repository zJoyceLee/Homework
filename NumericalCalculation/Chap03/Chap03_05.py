def factorization(num):
    factors=[]
    lastResult=num
    while True:
        if lastResult == 1:
            break
        c=2
        while True:
            if lastResult%c == 0:
                break
            c+=1
        factors.append(c)
        lastResult/=c
    return factors

num=int(input("Please enter a num(<1000): "))
print(factorization(num))
