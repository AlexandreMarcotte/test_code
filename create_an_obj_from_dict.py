class ObjFromDict:
    def __init__(self, d):
        self.__dict__ = d

d = {'dog': 10, 'cat':6, 'fish':100}

ofd = ObjFromDict(d)
print(ofd.dog)
print(ofd.cat)
