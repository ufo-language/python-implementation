from alltypes.object import Object
from ufo_exception import UFOException

class ScopeResolution (Object):

    __slots__ = ('_segments')

    def __init__(self, segments):
        self._segments = segments

    @staticmethod
    def from_parser(parse_value):
        return ScopeResolution(parse_value)

    def eval_rec(self, etor):
        collection = None
        first_iter = True
        for segment in self._segments:
            if first_iter:
                collection = segment.eval(etor)
                first_iter = False
            else:
                collection1 = collection.get(segment)
                if collection1 is None:
                    raise UFOException("Scope resolution operator could not find key in map",
                                       key=segment, map=collection)
                collection = collection1
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
