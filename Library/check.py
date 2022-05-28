from listbook import listbooks


class check:
    def __init__(self, id=0):
        self.name = input('Введите название:  ')
        self.sr_name()

        self.author = input('Введите автора:  ')
        self.sr_author()

        self.year = input('Введите год:  ')
        self.sr_year()

        self.number = input('Введите ISO:  ')
        self.sr_number()

        self.id = id

    def sr_name(self):
        while self.name.replace(' ', '') == '':
            print('\nERROR: Название книги не может быть пустой строкой.')
            print('___________________________________________________________________________________')
            self.name = input('Введите название:  ')
        return self.name

    def sr_author(self):
        while (self.author.replace(' ', '') == '') or (self.author.isnumeric() == True):
            if self.author.replace(' ', '') == '':
                print('\nERROR: Книга не может быть без автора.')
                print('___________________________________________________________________________________')
            if (self.author.isnumeric() == True):
                print('\nERROR: Книга не может быть цифрой.')
                print('___________________________________________________________________________________')
            self.author = input('Введите автора:  ')
        return self.author

    def sr_year(self):
        try:
            return int(self.year)
        except:
            while (not isinstance(self.year, int)) or (str(self.year).replace(' ', '')):
                print('\nERROR: Книга не может быть без года издания или строкой, введите число.')
                print('___________________________________________________________________________________')
                try:
                    self.year = int(input('Введите год издания:  '))
                    return self.year
                except:
                    pass

    def sr_number(self):
        while self.number.replace(' ', '') == '':
            print('\nERROR: Книга не может быть без ISO.')
            print('___________________________________________________________________________________')
            self.number = input('Введите ISO:  ')
        return self.number

    def result(self):
        return listbooks(self.name, self.author, self.year, self.number, self.id)