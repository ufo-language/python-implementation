import alltypes.data.binding
from alltypes.data._show_elems import show_elems
from alltypes.object import Object

class HashTable (Object):

    __slots__ = ('_hash',)

    def __init__(self):
        self._hash = {}

    @staticmethod
    def from_parser(parse_value):
        elems = parse_value
        hash_table = HashTable()
        for elem in elems:
            if not isinstance(elem, alltypes.data.binding.Binding):
                # I think this should never happen as long as the parser does its job.
                raise Exception(f"HashTable expected Binding, found {elem} :: {elem.type_name()}")
            hash_table[elem.lhs()] = elem.rhs()
        return hash_table

    def bool_value(self):
        return len(self._hash) > 0

    def eval_rec(self, etor):
        hash = HashTable()
        for (key, value) in self._hash.items():
            key_value = etor.eval(key)
            value_value = etor.eval(value)
            hash[key_value] = value_value
        return hash

    def __getitem__(self, key):
        return self._hash[key]

    def __setitem__(self, key, value):
        self._hash[key] = value

    def type_name(self):
        return 'HashTable'
    
    def show(self, stream):
        stream.write('#{')
        keys = sorted(self._hash.keys())
        first_iter = True
        for key in keys:
            if first_iter:
                first_iter = False
            else:
                stream.write(', ')
            key.show(stream)
            stream.write(alltypes.data.binding.Binding.CHAR)
            value = self._hash[key]
            value.show(stream)
        stream.write('}')
