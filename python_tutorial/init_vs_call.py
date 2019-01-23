class FooInit:
    def __init__(self, a, b):
        self.a = a
        self.b = b


class FooCall:
    def __call__(self, a, b):
        self.a = a
        self.b = b


f1 = FooInit(1, 2)
f2 = FooCall()
f2(3, 4)
print(f1 is f2)

