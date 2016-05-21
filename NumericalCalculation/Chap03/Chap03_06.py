def  sum_odd_1(n):
    odd_sum = 0
    for i in range(0, n):
        if i % 2 != 0:
            odd_sum += i
    return odd_sum

def sum_odd_2(n):
    # 2*x +n/2 = (1+n)*n/2
    return n*n/4


print(sum_odd_1(100))
print(sum_odd_2(100))
