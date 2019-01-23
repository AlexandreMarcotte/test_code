

class Base:
    def __init__(self):
        pass

    def print_cool(self):
        for _ in range(10):
            print('cool')

class A(Base):
    def print_cool(self):
        super().print_cool()
        print('A')


class B(Base):
    def print_cool(self):
        print('B')



a = A()
a.print_cool()