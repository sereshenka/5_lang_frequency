import os
import re
import argparse
from collections import Counter

def read_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('--file', help='Укажите путь к файлу ', nargs = '?')
    file_path = parser.parse_args().file
    return (existence_of_arguments(file_path, parser))

def existence_of_arguments(file_path, parser):
    if not file_path:
        parser.print_help()
        return None
    else:
        return (file_path)

        
def load_data(file):
    if not os.path.exists(file):
        print ('Неверный путь до файла\файла не существует,перезапустите программу и введите правильные данные')
        return None
    else:
        return (open_txt(file))
    
        
def open_txt(file):
    try:
        with open(file, 'r', encoding = 'utf-8') as file_handler:
            return (file_handler.read())
    except ValueError :
        print('Фаил нельзя прочитать')
        return None


def get_most_frequent_words(text):
    p = re.compile("([a-zA-Zа-яА-Я-']+)")
    all_words = p.findall(text)
    return (frequent_dictionary(all_words))

def frequent_dictionary(all_words):
    dictionary = Counter()
    for key in all_words:
        key = key.lower()
        dictionary[key] += 1
    return (dictionary)
        
        

def sort(dictionary):
    sorted_keys = sorted(dictionary,key = lambda x: int(dictionary[x]), reverse = True)
    return (sorted_keys)

def print_most_10_words(sorted_dictionary):
    i = 0
    print('Десять саммых популярных слов:')
    for key in sorted_dictionary:
        if i <= 9:
            s = str("{0}-{1}раз").format(key, dictionary[key])
            i += 1
            print (s)


if __name__ == '__main__':
    file_path = read_arguments()
    if file_path is not None:
        file = load_data(file_path)
        if file is not None:        
            dictionary = get_most_frequent_words(file)
            sorted_dictionary = sort(dictionary)
            print_most_10_words(sorted_dictionary)
            
