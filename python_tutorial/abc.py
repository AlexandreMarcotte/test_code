from abc import ABC, abstractmethod


class AbcEx(ABC):

    def __init__(self, value):
        self.value = value
        super().__init__()

    @abstractmethod
    def do_something(self):
        pass



class B(AbcEx):
    def do_something(self):
        print('B', self.value)


class A(AbcEx):
    def do_something(self):
        print('A', self.value)


def main():
    a = A(10)
    a.do_something()
    b = B(15)
    b.do_something()

if __name__ == '__main__':
    main()
