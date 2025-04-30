from alltypes.object import Object

class BinOp (Object):

    __slots__ = ('_lhs', '_oper', '_rhs')

    def __init__(self, lhs, oper, rhs):
        self._lhs = lhs
        self._oper = oper
        self._rhs = rhs

    @staticmethod
    def from_parser(parse_value):
        return BinOp(*parse_value)

    def eval_rec(self, etor):
        assert False
    
    def show(self, stream):
        self._lhs.show(stream)
        stream.write(' ')
        self._oper.show(stream)
        stream.write(' ')
        self._rhs.show(stream)

    def type_name(self):
        return 'BinOp'
