import conclusion


class library:
    def __init__(self, mas, id):
        self.mas = mas
        self.id = id

    def adde(self, new_id):
        self.id = new_id
        self.mas.append(conclusion.read_book(self.id))
        return 'Книга была успешно добавлена.'

    def show_dict(self):
        if len(self.mas) == 0:
            return ('В данный момент библиотека пуста.')
        else:
            print('Список книг:')
            return list(map(lambda x: str(
                str(x.get_name()) + ' ' + str(x.get_author()) + ' ' + str(x.get_year()) + ' ' + str(
                    x.get_number()) + ' ' + str(x.get_id())), self.mas))

    def remove_book(self):
        if len(self.mas) == 0:
            return 'Библиотека пуста.'
        par = input('Введите ISO:  ')
        re = []
        for i in range(len(self.mas)):
            x = self.mas[i]
            if x.get_number() == par:
                sl = x, i
                re.append(sl)
        if len(re) == 1:
            self.mas.pop(re[0][-1])
            return 'Книга с ISO <' + str(par) + '> удалена'
        elif len(re) > 1:
            for item in re:
                xs, i = item
                print(str(str(i + 1) + ') ' + str(xs.get_name()) + ' ' + str(xs.get_author()) + ' ' + str(
                    xs.get_year()) + ' ' + str(xs.get_number()) + ' ' + str(x.get_id())))
            try:
                de = int(input('Введите номер для удаления:  '))
                self.mas.pop(de - 1)
                return 'Книга с ISO <' + str(par) + '> удалена'
            except:
                while (not isinstance(de, int)) or (str(de).replace(' ', '')):
                    print('\nERROR: индекс не может быть пустым, строкой или быть больше имеющихся, введите число.')
                    try:
                        de = int(input('Введите номер для удаления:  '))
                        self.mas.pop(de - 1)
                        return 'Книга с ISO <' + str(par) + '> удалена'
                    except:
                        pass
        return 'ERROR: Книга с ISO <' + str(par) + '> не найдена!'

    def search_book(self):
        if len(self.mas) == 0:
            return 'Библиотека пуста.'
        x = True
        while x == True:
            conclusion.search()
            src = input('Введите пармаетр поиска: ').replace(' ', '')
            print('___________________________________________________________________________________')
            if src == '':
                print('Введена пусная строка.')
                print('')
            if src == '5':
                x = False
                return 'Отмена поиска'
            if src == '1':
                par = input('Введите название:  ')
                pin = list(map(lambda x: str(
                    str(x.get_name()) + ' ' + str(x.get_author()) + ' ' + str(x.get_year()) + ' ' + str(
                        x.get_number()) + ' ' + str(x.get_id())),
                               filter(lambda p: par.lower() in p.get_name().lower(), self.mas)))
                if len(pin) == 0:
                    return 'ERROR: Книга с названием <' + par + '> не найдена!'
                return pin
            if src == '3':

                try:
                    par = input('Введите год:  ')
                    pin = list(map(lambda x: str(
                        str(x.get_name()) + ' ' + str(x.get_author()) + ' ' + str(x.get_year()) + ' ' + str(
                            x.get_number()) + ' ' + str(x.get_id())),
                                   filter(lambda p: int(par) == int(p.get_year()), self.mas)))
                    if len(pin) == 0:
                        return 'ERROR: Книга с таким годом <' + par + '> не найдена!'
                    return pin
                except:
                    return 'Введенный год не верен!'
            if src == '2':
                par = input('Введите автора:  ')
                pin = list(map(lambda x: str(
                    str(x.get_name()) + ' ' + str(x.get_author()) + ' ' + str(x.get_year()) + ' ' + str(
                        x.get_number()) + ' ' + str(x.get_id())),
                               filter(lambda p: par.lower() in p.get_author().lower(), self.mas)))
                if len(pin) == 0:
                    return 'ERROR: Книга с таким автором <' + par + '> не найдена!'
                return pin
            if src == '4':
                par = input('Введите ISO:  ')
                pin = list(map(lambda x: str(
                    str(x.get_name()) + ' ' + str(x.get_author()) + ' ' + str(x.get_year()) + ' ' + str(
                        x.get_number()) + ' ' + str(x.get_id())),
                               filter(lambda p: par.lower() in p.get_number().lower(), self.mas)))
                if len(pin) == 0:
                    return 'ERROR: Книга с таким ISO <' + par + '> не найдена!'
                return pin

    def change_book(self):
        if len(self.mas) == 0:
            return 'Библиотека пуста.'
        par = input('Введите id:  ')
        for xi in self.mas:
            if xi.get_id() == int(par):
                xi = conclusion.change_book(xi)
                return '\nКнига с id <' + str(par) + '> успешна изменена'
        return '\nERROR: Книга с id <' + str(par) + '> не найдена'