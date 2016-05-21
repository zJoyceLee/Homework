import random
lst=[]
for i in range(0, 1000):
    lst.append(random.randint(1, 100))
#    print(lst)
for i in range(1, 100):
    if i in lst:
        counter=lst.count(i)
        print("%d frequency of occurrence is : %d"%(i,counter))
