class BaseDate:

    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def get_year(self):
        self.year = str(self.year)
        return self.year

    def get_month(self):
        self.month = str(self.month)
        return self.month

    def get_day(self):
        self.day = str(self.day)
        return self.day

    def set_year(self, y):
        self.year = y
        return self.year

    def set_month(self, m):
        self.month = str(m)
        return str(self.month)

    def set_day(self, d):
        self.day = str(d)
        return self.day


class AmericanDate(BaseDate):

    def format(self):
        if len(self.get_day()) > 1 and len(self.get_month()) > 1:
            return f'{self.get_month()}.{self.get_day()}.{self.get_year()}'
        if len(self.get_day()) == 1 and len(self.get_month()) == 1:
            return f'0{self.get_month()}.0{self.get_day()}.{self.get_year()}'
        if len(self.get_day()) > 1 and len(self.get_month()) == 1:
            return f'0{self.get_month()}.{self.get_day()}.{self.get_year()}'
        if len(self.get_day()) == 1 and len(self.get_month()) > 1:
            return f'{self.get_month()}.0{self.get_day()}.{self.get_year()}'


class EuropeanDate(BaseDate):

    def format(self):
        if len(self.get_day()) > 1 and len(self.get_month()) > 1:
            return f'{self.get_day()}.{self.get_month()}.{self.get_year()}'
        if len(self.get_day()) == 1 and len(self.get_month()) == 1:
            return f'0{self.get_day()}.0{self.get_month()}.{self.get_year()}'
        if len(self.get_day()) > 1 and len(self.get_month()) == 1:
            return f'{self.get_day()}.0{self.get_month()}.{self.get_year()}'
        if len(self.get_day()) == 1 and len(self.get_month()) > 1:
            return f'0{self.get_day()}.{self.get_month()}.{self.get_year()}'


american = AmericanDate(2000, 4, 10)
european = EuropeanDate(2000, 4, 10)
print(american.format())
print(european.format())
