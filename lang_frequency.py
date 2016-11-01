#!/usr/bin/python
#-*- coding: utf-8 -*-


import os
import re
import sys
import argparse
from collections import Counter


def load_win_unicode_console():
    if sys.platform == 'win32':
        import win_unicode_console
        win_unicode_console.enable()


def read_arguments():
    """
    использую с join,чтобы программа работала при указании пути,в котором папка
    может содержать в названии пробел.(C:\\Users\\New User\\file.format)
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('--direction', help='Укажите путь к файлу ', nargs = '+')
    arguments = parser.parse_args().direction
    try :
        file_path = ' '.join(arguments)
    except TypeError:
        return None, parser
    return file_path, parser  

        
def load_data(file):
    if not os.path.exists(file):
        return None
    else:
        with open(file, 'r', encoding = 'utf-8') as file_handler:
            return file_handler.read().lower()
    
        
def get_most_frequent_words(text):
    p = re.compile("([a-zA-Zа-яА-Я-']+)")
    all_words = p.findall(text)
    return Counter(all_words)
    """
    можно было сразу найти 10 самых популярных слов:
    return Counter(all_words).most_common(10)
    но это будет не рационально,тк в других проектах,
    легче будет использовать эту функию и сделать выборку,если нужна
    """


def print_most_10_words(top10_of_dictionary):
    for indx, item in enumerate(top10_of_dictionary):
        print(("{}. {} - {} раз(а)").format(indx+1, item[0], item[1]))


if __name__ == '__main__':
    while True:
        load_win_unicode_console()
        
        file_path,parser = read_arguments()
        if file_path is None:
            parser.print_help()
            break
        
        try:
            text = load_data(file_path)
        except ValueError:
            print('Фаил нельзя прочитать(неподдерживаемый формат фаила)')
            break
        if text is None:
            print ('Неверный путь до файла\файла не существует,перезапустите программу и введите правильные данные')
            break
        
        dictionary = get_most_frequent_words(text)
        top10_of_dictionary = dictionary.most_common(10)
        print_most_10_words(top10_of_dictionary)
        break
