import datetime as dt


class Date:

    def __init__(self, month, day):
        self.month = month
        self.day = day

    def __sub__(self, second):
        date1 = dt.date(2022, self.month, self.day)
        date2 = dt.date(2022, second.month, second.day)
        total_date = str(date1 - date2).split()
        if len(total_date) != 1:
            return total_date[0]
        else:
            return 0


mar5 = Date(3, 1)
jan1 = Date(1, 1)

print(mar5 - jan1)
print(jan1 - mar5)
print(jan1 - jan1)
print(mar5 - mar5)

jan5 = Date(1, 5)
jan1 = Date(1, 1)

print(jan5 - jan1)
print(jan1 - jan5)
print(jan1 - jan1)
print(jan5 - jan5)