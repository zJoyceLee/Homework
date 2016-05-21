import random
lst=[random.randint(0,100) for _ in range(0,20)]
print(lst)

a=lst[::2]
print(a)
a.sort(reverse=True)
print(a)

b=[lst[2*i+1] for i in range(0, len(lst)/2)]
print(b)

lst=[]
for i in range(0, len(a)):
    lst.append(a[i])
    lst.append(b[i])
print(lst)
