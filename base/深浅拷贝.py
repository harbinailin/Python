import copy

a = [1, 2, 3, ['a', 'b']]
b = a
c = copy.copy(a)
d = copy.deepcopy(a)
a.append(4)
a[3].append('c')
print('a = ', a)
print('b = ', b)
print('c = ', c)
print('d = ', d)

