import MySQLdb

db = MySQLdb.connect('localhost', 'root', '1', 'Words')
cursor = db.cursor()

def readFile(path):
    all_the_text = ''
    with open(path) as file_obj:
        all_the_text += file_obj.read()
        words = all_the_text.split()
        # print(words, type(words))
    return words

words = readFile('./words.txt')
print(words[:100])

for val in words:
    print(val, type(val))
    ss = "INSERT INTO Word(word, len) VALUES ('{0}', {1});".format(val, len(val))
    cursor.execute(ss)

sql = 'CREATE INDEX lenDESC on Word (word ASC, len DESC);'
cursor.execute(sql)

sql = 'CREATE VIEW Word_lenDESC AS SELECT * FROM Word ORDER BY 2 DESC, 1 ASC;'
cursor.execute(sql)

db.commit()
print('Create done.')
