import os
import sys
import collections
import re


def load_data(filepath):
    if not os.path.exists(filepath):
        print('Путь до файла указан не верно\не существует такого файла. Перезапустите,пожалуйста, программу')
        sys.exit()
        return None
    return open(filepath,'r')

def get_most_frequent_words(text):
    print('Укажите,пожалуйста, язык текста\n2-Русский\n1-Английский\n0-Выход')
    a=int(input())
    if a == 2 or a == 1 or a == 0:
        if a == 2:
            p = re.compile("([а-яА-Я-']+)")
        if a == 1:
            p = re.compile("([a-zA-Z-']+)")
        if a == 0:
            sys.exit()
    else:
        print('Вы непраивльно ввели цифру,перезапустите программу')
        sys.exit()
    i=0
    res = p.findall(text)
    isword = {}
    for key in res:
        key = key.lower()
        if key in isword:
            value = isword[key]
            isword[key] = value + 1
        else:
            isword[key] = 1
    sorted_keys = sorted (isword,key = lambda x: int(isword[x]), reverse = True)
    for key in sorted_keys :
        if i <= 9:
            s = str("{0}-{1}раз").format(key,isword[key])
            i+=1
            print (s)


if __name__ == '__main__':
    pass

direkt = input('Укажите пусть до фаила:')
file = load_data(direkt)
get_most_frequent_words(file.read())


file.close


