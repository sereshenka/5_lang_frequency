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


def input_path():
    parser = argparse.ArgumentParser()
    parser.add_argument('--path', help='Укажите путь к папке ', nargs = '?')
    file_path = parser.parse_args().path
    if file_path is None:
        parser.print_help()
    return file_path  

        
def load_data(file):
    with open(file, 'r', encoding = 'utf-8') as file_handler:
        return file_handler.read().lower()
    
        
def get_all_words_in_text(text):
    p = re.compile("([a-zA-Zа-яА-Я-']+)")
    all_words = p.findall(text)
    return all_words


def get_top10_words(all_words):
    dictionary = Counter(all_words)
    return dictionary.most_common(10)
    
    
def print_result(top10_words):
    for indx, item in enumerate(top10_words):
        print(("{}. {} - {} раз(а)").format(indx+1, item[0], item[1]))


if __name__ == '__main__':
    while True:
        load_win_unicode_console()
        
        file_path = input_path()
        if file_path is None:
            break
        if not os.path.exists(file_path):
            print('Неправильно указан путь\папка не существует')
            break
        
        try:
            text = load_data(file_path)
        except ValueError:
            print('Фаил нельзя прочитать(неподдерживаемый формат фаила)')
            break
        
        all_words = get_all_words_in_text(text)
        top10_words = get_top10_words(all_words)
        print_result(top10_words)
        break
