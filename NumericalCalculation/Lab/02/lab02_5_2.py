import re

def wordSplit(path):
    with open(path) as file_obj:
        all_the_text = file_obj.read().lower()
        all_the_text = re.sub('\"|,|\.|"|:|;|\?', " ", all_the_text)
        words = all_the_text.split()

    return words


def wordCounter(path):
    result = {}
    words = wordSplit(path)

    for  word in words:
        if  word not in result:
            result[word] = 0
        result[word] += 1

    return  result


if __name__ == '__main__':
    try:
        keys = wordSplit('./words.txt')
        values = [0 for _ in range(len(keys))]
        mydict = dict(zip(keys, values))

        all_word_info = wordCounter('./file.txt')
        for  key, val in mydict.items():
            val =  all_word_info.get(key)
            print(key, val)

    except(TypeError, NameError) as e:
        print(e)
