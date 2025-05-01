from alltypes.literal.nil import Nil
from alltypes.object import Object

class Subscript (Object):

    __slots__ = ('_collection', '_index')

    def __init__(self, collection, index):
        self._collection = collection
        self._index = index

    @staticmethod
    def from_parser(parse_value):
        return Subscript(*parse_value)

    def eval_rec(self, etor):
        collection_val = etor.eval(self._collection)
        index_val = etor.eval(self._index)
        return collection_val.get(index_val)
    
    def show(self, stream):
        self._collection.show(stream)
        stream.write('[')
        self._index.show(stream)
        stream.write(']')

    def type_name(self):
        return 'Subscript'
