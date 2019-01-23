from abc import ABCMeta, abstractmethod


class A(metaclass=ABCMeta):
    def __init__(self):
        self.data = [1,2,3]

    def spam(self):
        print('A.spam')


class B(A):
    A.__new__(A)
    def spam(self):
        print('B.spam')
        super().spam()


class C(B):
    def spam(self):
        print('C.spam')
        super().spam()



a = A()
a.data.append(99)

c = C()
c.spam()
print(c.data)
c.data.append(4)
print('c.data', c.data)
print('a.data', a.data)

