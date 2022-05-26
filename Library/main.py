from colorama import Fore, Back, Style
from source.storage.csv import Library
from source.models.cli import *
import os
import sys


def __error(*args, **kwargs):
    print(Fore.RED, *args, Style.RESET_ALL, **kwargs)

def __info(*args, **kwargs):
    print(Fore.GREEN , *args, Style.RESET_ALL, **kwargs)


MAX_LEN = 79

def __print_list(title, items):
    print(title)
    print('-' * MAX_LEN)
    print('   ID | Type     | Name')
    print('-' * MAX_LEN)
    for _id, media in items:
        print('{} | {} | {}'.format( 
            str(_id).rjust(5, ' '), 
            str(media.type).ljust(8, ' '),
            media.short
        ))
        print('-' * MAX_LEN)


def __get_media():
    _id = None
    while not isinstance(_id, int):
        try:
            _id = int(input('Enter ID of media: '))
        except:
            continue
        else:
            break
    media = library.get_one_by_id(_id)
    if media is None:
        __error(f'  ERROR: media with id {_id} is not exists')
        return
    return (_id, media)
    

def __input_data_of_object(obj):
    for key, data in obj.fields.items():
        while True:
            try:
                template = 'Enter ' + data.get('title')
                prev = getattr(obj, key)
                if prev:
                    template += f' [{str(prev)}]'
                value = input(template + ': ')
                setattr(obj, key, value)
                break
            except Exception as e:
                __error('  ERROR: ' + str(e))


library = Library(config={
    "file": os.path.abspath(os.curdir) + "/data/library.csv",
    "classes": [Book, Link, Video, Audio]
})

def menu():
    cmd = {
        "1": {
            "name": "List of media",
            "callback": media_list
        },
        "2": {
            "name": "Open media",
            "callback": media_open
        },
        "3": {
            "name": "Search media",
            "callback": media_search
        },
        "4": {
            "name": "Add media",
            "callback": media_add
        },
        "5": {
            "name": "Update media",
            "callback": media_update
        },
        "6": {
            "name": "Delete media",
            "callback": media_delete
        },
        "0": {
            "name": "Exit",
            "callback": exit
        }
    }
    print('=' * MAX_LEN)
    for key, value in cmd.items():
        __info('{}] {}'.format(key, value.get('name')))
    print('=' * MAX_LEN)
    user_cmd = None
    while user_cmd not in cmd.keys():
        user_cmd = input('Select option: ')
    info = cmd.get(user_cmd)
    print('=' * MAX_LEN)
    info.get("callback")()


def media_list():
    __print_list('List of media', library.all())


def media_open():
    media = __get_media()
    if media is None:
        return
    print('-' * MAX_LEN)
    print(media[1].full)


def media_add():
    print('Available sources: ' + ', '.join(library.types))
    user_cmd = None
    while user_cmd not in library.types:
        user_cmd = input('What do you want to add: ')
    obj = library.get_class_by_type(user_cmd)
    if obj is None:
        __error(f'Type "{user_cmd} is not exists')
        return
    print(f'---Adding {user_cmd[0].upper() + user_cmd[1:]}--')
    obj = obj()
    __input_data_of_object(obj)
    library.save(obj)
    print('-' * MAX_LEN)
    __info('Success!')


def media_update():
    media = __get_media()
    if media is None:
        return
    _id, obj = media
    __input_data_of_object(obj)
    library.save(obj, _id)
    print('-' * MAX_LEN)
    __info('Success!')


def media_delete():
    media = __get_media()
    if media is None:
        return
    _id, obj = media
    library.delete(_id)
    print('-' * MAX_LEN)
    __info('Success!')


def media_search():
    query = input('Enter query for search: ').strip()
    if not query:
        return
    items = library.find(query)
    __print_list('Resulf of search', items)


def exit():
    print('Exit from application')
    sys.exit()


while True:
    menu()
