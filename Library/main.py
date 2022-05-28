from lib import library
from conclusion import res, menu, ex, pars_book, save_book
import json


def main():
    s = True
    try:
        with open('storage.json') as file:
            xs = json.load(file)
    except:
        xs = None
    ch, mas = pars_book(xs)
    while s != False:
        a = library(mas, ch)
        menu()
        x = str(input('Введите команду: ')).replace(' ', '')
        print('  ')
        if x == '1':
            print('='*79)
            res(a.adde(ch))
            ch += 1
        elif x == '2':
            print('='*79)
            res(a.show_dict())
        elif x == '3':
            print('='*79)
            print(a.remove_book())
        elif x == '4':
            print('='*79)
            res(a.search_book())
        elif x == '5':
            print('='*79)
            res(a.change_book())
        elif x == '6':
            s = False
            save_book(a.mas, a.id)
            ex()
        else:
            print('='*79)
            print('Введеная команда не найдена!')


main()
