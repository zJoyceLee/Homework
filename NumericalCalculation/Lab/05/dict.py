def count(x):
    fin=open(r'3.txt','r')
    sep=''
    wordlist=[]
    for line in fin:
        word=line.strip()
        wordlist.append(word)
    article=sep.join(wordlist)
    #print (article.find('第八十一回'))
    num=article.count(x)
    fin.close()
    return num


def dictionary():
    key=['而','何','乎','乃','其','且','若','所','為'
         ,'焉','也','以','因','于','与','则','者','之']
    values=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    d=dict(zip(key,values))
    for k in key:
        d[k]=count(k)
    with open('result.txt','w') as f:
        f.write(str(d))
    return d

dictionary()
