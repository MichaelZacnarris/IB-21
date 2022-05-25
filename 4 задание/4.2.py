class ReversedList(object):

    def __init__(self, ls):
        self.l = list(reversed(ls))

    def __str__(self):
        return str(self.l)

    def __len__(self):
        return len(self.l)

    def __getitem__(self, i):
        return self.l[i]


rl = ReversedList([10, 20, 30])
for i in range(len(rl)):
    print(rl[i])

rl = ReversedList([])
print(len(rl))

rl = ReversedList([10])
print(len(rl))
print(rl[0])