from alltypes.object import Object

class ScopeResolution (Object):

    __slots__ = ('_segments')

    def __init__(self, segments):
        self._segments = segments

    @staticmethod
    def from_parser(parse_value):
        return ScopeResolution(parse_value)

    def eval_rec(self, etor):
        print("ScopeResolution.eval_rec", self)
        collection = {}
        first_iter = True
        for segment in self._segments:
            if first_iter:
                collection = etor.lookup(segment)
            else:
                collection = collection.get(segment)
        return collection
    
    def show(self, stream):
        first_iter = True
        for segment in self._segments:
            if first_iter:
                first_iter = False
            else:
                stream.write(':')
            segment.show(stream)

    def type_name(self):
        return 'ScopeResolution'
