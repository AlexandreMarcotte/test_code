from collections import namedtuple

Btn_pos = namedtuple('position', ['row', 'col', 'rowspan', 'colspan'])

b_p = Btn_pos(10, 10, 100, 100)

x,y,z,a = b_p

print('x', x, 'y', y, 'z', z, 'a', a)