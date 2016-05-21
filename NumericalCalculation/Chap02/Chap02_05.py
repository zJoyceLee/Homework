import random
lst=[]
for i in range(0,20):
    lst.append(random.randint(0,100))
print(lst)

lst_1=lst[:10]
lst_1.sort()
print(lst_1)

lst_2=lst[10:]
lst_2.sort(reverse=True)
print(lst_2)

lst_1.extend(lst_2)
print(lst_1)
