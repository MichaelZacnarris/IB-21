from check import check
from change import changeb
from listbook import listbooks
from parsing import parsing
from load import pars
from colorama import Fore

def res(llist):
    if type(llist) == list:
        ch = 1
        for row in llist:
            print(str(ch) + ')', str(row))
            ch += 1
    else:
        print(llist)


def read_book(id):
    return check(id).result()

def change_book(book=listbooks):
    return changeb(book).result()

def pars_book(book):
    return parsing.parse(book)

def save_book(book, id):
    pars.save(book, id)



def menu():
    print(Fore.BLUE,"||",'='*77, "||")
    print("||",'                        Библиотека "Синяя синичка"                              ',"||")
    print("||",'                                        ',"                                       ","||")
    print("||",' Доступные команды:',"                                                            ","||")
    print("||",'   1] Добавить                                                                  ',"||")
    print("||",'   2] Вывести список                                                            ',"||")
    print("||",'   3] Удалить                                                                   ',"||")
    print("||",'   4] Поиск                                                                     ',"||")
    print("||",'   5] Изменить                                                                  ',"||")
    print("||",'   6] Выход                                                                     ',"||")
    print(" ||",'='*77, "||")


def ex():
    print('='*79)
    print('             Библиотека "Синяя синичка" была закрыта')
    print('='*79)
    print()



def search():
    print("||",'='*79, "||")
    print(' Доступные команды:')
    print('   1] Поиск по имени    ')
    print('   2] Поиск по автору   ')
    print('   3] Поиск по году     ')
    print('   4] Поиск по ISO >')
    print('   5] Выход             ')
    print("||",'='*79, "||")