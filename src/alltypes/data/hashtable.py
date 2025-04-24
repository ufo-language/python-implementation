from alltypes.object import Object

class HashTable (Object):

    __slots__ = ('_hash',)

    def __init__(self):
        self._hash = {}

    @staticmethod
    def from_python_list(python_list):
        queue = HashTable()
        for elem in python_list:
            assert False
        return hash

    def type_name(self):
        return 'HashTable'

    def __repr__(self):
        assert False
