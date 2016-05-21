import MySQLdb

db = MySQLdb.connect('localhost', 'root', '1', 'Words')
cursor = db.cursor()

ss = 'SELECT * FROM Word_lenDESC;'
cursor.execute(ss)
results = cursor.fetchall()


def isInDict(word):
    ss = "SELECT * FROM Word_lenDESC WHERE word = '{0}';".format(word)
    cursor.execute(ss)
    result = cursor.fetchall()
    if result is ():
        return False
    else:
        return True

def isTarget(s):
    print(s)
    slen = len(s)
    one_char_less_list = [s[:i]+s[i+1:] for i in range(slen) if isInDict(s[:i]+s[i+1:])]

    if slen == 0 or slen == 1:
        return (s,)
    else:
        ret = ()
        for substr in one_char_less_list:
            ret += (isTarget(substr),)
        return (s,) + ret

# lst = []
# ss = 'INSERT INTO Target(word, len) VALUES '
# for word in results:
#     myWord = word[0]
#     # print(myWord)
#     if isTarget(myWord):
#         lst.append(myWord)
#         # sql = ss+"('{0}', {1});".format(myWord, len(myWord))
#         # cursor.execute(sql)
# # db.commit()
# print(lst)
print(isTarget('complecting'))
