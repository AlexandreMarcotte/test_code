class FFTGraph(object):
    def __init__(self):
        self.x = 'FFTGraph'


class EEGGraph(object):
    def __init__(self):
        self.y = 'EEGGraph'


class MultiGraph(FFTGraph, EEGGraph):
    def __init__(self):
        FFTGraph.__init__(self)
        EEGGraph.__init__(self)
        self.z = 'MULTIGraph'

    def print_sub_class_var(self):
        print('x', self.x)
        print('y', self.y)
        print('Z', self.z)


multi_graph = MultiGraph()
multi_graph.print_sub_class_var()
