class SparseArray:  # __getitem__(self, item) – получение значения по ключу item;
    # __setitem__(self, key, value) – запись значения value по ключу key;
    # __delitem__(self, key) – удаление элемента по ключу key.

    def __init__(self):
        self.data = {}

    def __getitem__(self, key):
        return self.data.get(key, 0)

    def __setitem__(self, key, value):
        self.data[key] = value

arr = SparseArray()
arr[1] = 10
arr[8] = 20
for i in range(10):
    print('arr[{}] = {}'.format(i, arr[i]))

arr = SparseArray()
arr[10] = 123
for i in range(8, 13):
    print('arr[{}] = {}'.format(i, arr[i]))

def print_elem(array, ind):
    print('arr[{}] = {}'.format(ind, array[ind]))

arr = SparseArray()
index = 1000000000
arr[index] = 123

print_elem(arr, index - 1)
print_elem(arr, index)
print_elem(arr, index + 1)
