class MinStat:
    def __init__(self):
        self.stat = []

    def add_number(self, i):
        self.stat.append(i)

    def result(self):
        if self.stat == []:
            return
        else:
            return min(self.stat)


class MaxStat:
    def __init__(self):
        self.stat = []

    def add_number(self, i):
        self.stat.append(i)

    def result(self):
        if self.stat == []:
            return
        else:
            return max(self.stat)


class AverageStat:
    def __init__(self):
        self.stat = []

    def add_number(self, i):
        self.stat.append(i)

    def result(self):
        if self.stat == []:
            return
        else:
            llen = len(self.stat)
            ssum = sum(self.stat)
            return llen / ssum


values = [1, 2, 4, 5]

mins = MinStat()
maxs = MaxStat()
average = AverageStat()
for v in values:
    mins.add_number(v)
    maxs.add_number(v)
    average.add_number(v)

print(mins.result(), maxs.result(), '{:<05.3}'.format(average.result()))