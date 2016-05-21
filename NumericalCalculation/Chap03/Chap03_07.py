def foo(x):
    if x < 0:
        y = 0
    elif x >= 0 and x < 5:
        y = x
    elif x >= 5 and x <10:
        y = 3 * x - 5
    elif x >=10 and x < 20:
        y = 0.5  *x - 2
    else:
        y = 0
    return y

print(foo(-2))
print(foo(3))
print(foo(7))
print(foo(15))
print(foo(22))
