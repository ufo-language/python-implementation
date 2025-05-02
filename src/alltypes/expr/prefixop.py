from alltypes.expr.apply import Apply
from alltypes.expr.binop import BinOp
from alltypes.object import Object

class PrefixOp (Object):

    __slots__ = ('_oper', '_rhs', '_apply')

    def __init__(self, oper, rhs):
        self._oper = oper
        self._rhs = rhs
        self._apply = Apply(oper, [rhs])

    @staticmethod
    def from_parser(parse_value):
        op = parse_value[0]
        rhs = parse_value[1]
        return PrefixOp(*parse_value)

    def eval_rec(self, etor):
        return self._apply.eval(etor)
    
    def show(self, stream):
        self._oper.show(stream)
        stream.write(' ')
        if type(self._rhs) is BinOp:
            stream.write('(')
            self._rhs.show(stream)
            stream.write(')')
        else:
            self._rhs.show(stream)

    def type_name(self):
        return 'PrefixOp'
