from time import time

num = 100000


start_t = time()
# ITTERATOR
# Pipelines functions
def generate_data():
    for value in range(num):
        print('generate_data')
        yield value

def add_val(value):
    for val in value:
        print('add_val')
        yield val + 10

def mult_val(value):
    for val in value:
        print('mult_val')
        yield 10 * val

# Pipeline
value = generate_data()
value = add_val(value)
value = mult_val(value)

for val in value:
    print(val)

print(time()-start_t)

# %%
# CLASIC
# Pipelines functions
start_t = time()

def generate_data():
    v = []
    for val in range(num):
        print('generate_data')
        v.append(val)
    return v

def add_val(value):
    v = []
    for val in value:
        print('add_val')
        v.append(val+10)
    return v

def mult_val(value):
    v = []
    for val in value:
        print('mult_val')
        v.append(10*val)
    return v

# Pipeline
value = generate_data()
value = add_val(value)
value = mult_val(value)

for val in value:
    print(val)

print(time()-start_t)



#%%
from time import time

start_t = time()

def generate_data():
    num = 100000
    for value in range(num):
        yield value

def add_val():
    yield from generate_data() + 10

def mult_val():
    yield from add_val() * 10

value = mult_val()

for val in value:
    print(val)

print(time()-start_t)

#%%
num = 10000000

from time import time

x = []
start_t = time()
for i in range(num):
    x.append(i)
print(time()-start_t)



#%%
start_t = time()
x = [i for i in range(num)]
print(time()-start_t)

#%%
from time import time

num = 100000
start_t = time()

def generate_data():
    for value in range(num):
        yield value

def add_val(value):
    for val in value:
        yield val + 10

def mult_val(value):
    for val in value:
        yield 10 * val

# Pipeline
value = generate_data()
value = add_val(value)
value = mult_val(value)

for val in value:
    print(val)

print('elapsed time: ', time()-start_t)

#%%
import tensorflow
import keras

class Epicerie:
    def __init__(self, pain, pate, patate) :
        self.pain = pain
        self.pate = pate
        self.patate = patate

    def __add__(self, other):
        print('pain', self.pain + other.pain,
              'pate', self.pate + other.pate,
              'patate', self.patate + other.patate)

    def __str__(self):
        return str(self.pain)

    def __repr__(self):
        return ('pain: ' + str(self.pain) + '\n' +
                'pate: ' + str(self.pate) + '\n' +
                'patate: ' + str(self.patate))

e1 = Epicerie(3, 3, 3)
e2 = Epicerie(1, 1, 1)


#%%
class Root:
    def __init__(self, var1, var2, var3):
        self.var1 = var1
        self.var2 = var2
        self.var3 = var3

    def func1(self):
        self.var1 += 1

class Branch(Root):
    def __init__(self, var4, var5, *args):
        super().__init__(*args)
        self.var4 = var4
        self.var5 = var5

    def func2(self):
        pass

b = Branch(4, 5)



