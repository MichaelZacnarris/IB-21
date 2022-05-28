from listbook import listbooks


class changeb:
    def __init__(self, eldlistbooks=listbooks):
        self.eldlistbooks = eldlistbooks

        self.name = input(f'Введите название(или оставить "{self.eldlistbooks.get_name()}"):  ')
        self.ch_name()

        self.author = input(f'Введите автора(или оставить "{self.eldlistbooks.get_author()}"):  ')
        self.ch_author()

        self.year = input(f'Введите год(или оставить "{self.eldlistbooks.get_year()}"):  ')
        self.ch_year()

        self.number = input(f'Введите артикул(или оставить "{self.eldlistbooks.get_number()}"):  ')
        self.ch_number()

    def ch_name(self):
        if self.name != '':
            self.eldlistbooks.set_name(self.name)

    def ch_author(self):
        if self.author != '':
            while (self.author.replace(' ', '') == '') or (self.author.isnumeric() == True):
                if self.author.replace(' ', '') == '':
                    print('\nERROR: Книга не может быть без автора!')
                    print('___________________________________________________________________________________')
                if (self.author.isnumeric() == True):
                    print('\nERROR: Книга не может быть цифрой!')
                    print('___________________________________________________________________________________')
                    self.author = input('Введите автора:  ')
            self.eldlistbooks.set_author(self.author)

    def ch_year(self):
        if self.year != '':
            try:
                self.eldlistbooks.set_year(int(self.year))
            except:
                while (not isinstance(self.year, int)) or (str(self.year).replace(' ', '')):

                    print('\nERROR: Книга не может быть без года издания или строкой, введите число!')
                    print('___________________________________________________________________________________')
                    try:
                        self.eldlistbooks.set_year(int(input('Введите год издания:  ')))
                        break
                    except:
                        pass

    def ch_number(self):
        if self.number != '':
            self.eldlistbooks.set_number(self.number)

    def result(self):
        return self.eldlistbooks