def modify_word(word):
    ss = ''
    for i in range(0, len(word)):
        if word[i] == 'I' and len(word) != 1:
            word[i] = 'i'
        ss  += word[i]
    return ss

def list2string(lst):
    ret = ''
    for i in range(0, len(lst) - 1):
        ret += lst[i] + ' '
    ret += lst[-1]
    return ret

ss="iaccdo eo uItI aeoaoehuau Ioosnio Iutuc i nsh I hhneh haInoiunoehi i nt i"
print(ss)
lst=ss.split()
print(lst)
for i in range(0,len(lst)):
    lst[i] = modify_word(list(lst[i]))
print(lst)
modified_ss = list2string(lst)
print(modified_ss)
