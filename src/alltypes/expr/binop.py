from alltypes.expr.apply import Apply
from alltypes.object import Object

class BinOp (Object):

    __slots__ = ('_lhs', '_oper', '_rhs', '_apply')

    def __init__(self, lhs, oper, rhs):
        self._lhs = lhs
        self._oper = oper
        self._rhs = rhs
        self._apply = Apply(oper, [lhs, rhs])

    @staticmethod
    def from_parser(parse_value):
        lhs = parse_value[0]
        op = parse_value[1]
        rhs = parse_value[2]
        return BinOp(*parse_value)

    def eval_rec(self, etor):
        return self._apply.eval(etor)
    
    def show(self, stream):
        if type(self._lhs) is BinOp:
            stream.write('(')
            self._lhs.show(stream)
            stream.write(')')
        else:
            self._lhs.show(stream)
        stream.write(' ')
        self._oper.show(stream)
        stream.write(' ')
        if type(self._rhs) is BinOp:
            stream.write('(')
            self._rhs.show(stream)
            stream.write(')')
        else:
            self._rhs.show(stream)

    def type_name(self):
        return 'BinOp'
