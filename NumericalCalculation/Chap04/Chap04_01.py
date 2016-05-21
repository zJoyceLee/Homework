def list2string(lst):
    ret = ''
    for i in range(0, len(lst) - 1):
        ret += lst[i] + ' '
    ret += lst[-1]
    return ret

ss="iaccdo eo uiti aeoaoehuau ioosnio iutuc i nsh I hhneh hainoiunoehi i nt i"
print(ss)
lst=ss.split()
print(lst)
for i in range(0,len(lst)):
    if lst[i] == 'i':
        lst[i] = 'I'

print(lst)
modified_ss = list2string(lst)[]
print(modified_ss)
