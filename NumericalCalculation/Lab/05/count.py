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
