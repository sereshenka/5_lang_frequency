import os
import sys
import re

def input1():
    try:
        n = int(input('Укажите,пожалуйста, язык текста\n2-Русский\n1-Английский\n0-Выход\n'))
        return (n)
    except ValueError:
        n = None
    if n is None:
        print('Неверный формат ввода')

def load_data(filepath):
    if not os.path.exists(filepath):
        print('Путь до файла указан не верно\не существует такого файла. Перезапустите,пожалуйста, программу')
        return None
    else:
        return(open(filepath,'r'))
        
        

def language(n):
    if n == 2 or n == 1 or n == 0:
        if n == 2:
            p = re.compile("([а-яА-Я-']+)")
            return (p)
        if n == 1:
            p = re.compile("([a-zA-Z-']+)")
            return (p)
        if n == 0:
            sys.exit()
    else:
        print('Вы непраивльно ввели цифру,перезапустите программу')
        return None


def open_txt(file):
    try:
        return(file.read())
    except (IOError,ValueError):
        print ('Неправильный формат файла')
        return None

def get_most_frequent_words(text,p):
    res = p.findall(text)
    isword = {}
    for key in res:
        key = key.lower()
        if key in isword:
            value = isword[key]
            isword[key] = value + 1
        else:
            isword[key] = 1
    return (isword)

def sorting(isword):
    i=0
    sorted_keys = sorted (isword,key = lambda x: int(isword[x]), reverse = True)
    for key in sorted_keys :
        if i <= 9:
            s = str("{0}-{1}раз").format(key,isword[key])
            i+=1
            print (s)


if __name__ == '__main__':
    direkt = input('Укажите пусть до фаила:')
    file = load_data(direkt)
    if file is not None:
        n = input1()
        if n is not None:        
            p = language(n)
            if p is not None:
                text = open_txt(file)
                if text is not None:
                    dictionary = get_most_frequent_words(text,p)
                    file.close
                    sorting(dictionary)
