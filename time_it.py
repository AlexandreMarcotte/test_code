import timeit
from functools import partial

def list_comprehension(a):
    a = 10
    for i in [b for b in range(10000)]:
        x = i**2


print(timeit.timeit(partial(list_comprehension, 10), number=1000))

