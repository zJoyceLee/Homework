import random
lst=[random.randint(0,100) for _ in range(0,50)]
print("Origin list: " +str(lst))

def del_odd_from_back(lst):
    end=len(lst)
    for j in range(0,end):
        last_index=len(lst)-1
        for i in range(last_index,-1,-1):
            if lst[i]%2!=0:
                lst.pop(i)
                print(lst)
                break;

def del_odd(lst):
    return [lst[i] for i in range(0,len(lst)) if lst[i]%2==0]

lst1=lst[:]
lst1=del_odd(lst1)
print("Result list: "+str(lst1))

del_odd_from_back(lst)
print("Result list: "+str(lst))
