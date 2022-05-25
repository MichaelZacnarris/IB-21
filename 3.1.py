class LeftParagraph:

    def __init__(self, num=int()):
        self.num = num
        self.counter = []

    def add_word(self, strr=str()):

        if len(self.counter) == 0 or len(strr + self.counter[-1]) >= self.num:
            self.counter.append(strr)
        else:
            self.counter[-1] = self.counter[-1] + ' ' + str(strr)

    def end(self):
        for i in self.counter:
            print(i)


class RightParagraph:

    def __init__(self, num=int()):
        self.num = num
        self.counter = []

    def add_word(self, strr=str()):

        if len(self.counter) == 0 or len(strr + (self.counter[-1]).lstrip()) >= self.num:
            self.counter.append(strr.rjust(self.num, ' '))


        else:
            self.counter[-1] = (self.counter[-1].lstrip() + ' ' + str(strr)).rjust(self.num, ' ')

    def end(self):
        for i in self.counter:
            print(i)

lp = LeftParagraph(8)
lp.add_word('abc')
lp.add_word('defg')
lp.add_word('hi')
lp.add_word('jklmnopq')
lp.add_word('r')
lp.add_word('strruv')
lp.end()
print()

rp = RightParagraph(8)
rp.add_word('abc')
rp.add_word('defg')
rp.add_word('hi')
rp.add_word('jklmnopq')
rp.add_word('r')
rp.add_word('strruv')
rp.end()
print()