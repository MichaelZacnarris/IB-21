from classes.BoardClass import Board
from functions import COLOR_BLACK, COLOR_WHITE, get_point


def main():
    board = Board(COLOR_WHITE)
    while True:
        board.draw()
        print('Команды:')
        print('    exit                             -- выход')
        print('    move <row><col> <row1><col1>     -- ход из клетки (row, col)')
        print('                                        в клетку (row1, col1)')
        if board.current_player() == COLOR_WHITE:
            print('Ход белых')
        else:
            print('Ход черных')
        command = input('Введите команду: ')
        data = command.split()
        if not len(data) or data[0] not in ['exit', 'move']:
            input('Неверная команда! Нажмите Enter для продолжения')
            continue
        if data[0] == 'exit':
            break
        if len(data) != 3:
            input('Неверное использование команды move! Нажмите Enter для продолжения')
            continue
        move_type, _from, _to = data
        point_from = get_point(_from)
        point_to = get_point(_to)
        if point_from is None or point_to is None:
            input('Неверный формат координат! Нажмите Enter для продолжения')
            continue
        from_row, from_col = point_from
        to_row, to_col = point_to
        if board.move(from_row, from_col, to_row, to_col):
            print('Ход успешен')
        else:
            input('Координаты некорректны! Попробуйте другой ход! Нажмите Enter для продолжения')


if __name__ == '__main__':
    main()
