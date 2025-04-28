from alltypes.data._show_elems import show_elems
from alltypes.literal.nil import Nil
from alltypes.object import Object

class Seq (Object):

    __slots__ = ('_exprs')

    def __init__(self, exprs):
        self._exprs = exprs

    @staticmethod
    def from_parser(parse_value):
        return Seq(parse_value)

    def eval_rec(self, etor):
        value = Nil()
        saved_env = etor.env_save()
        for expr in self._exprs:
            value = etor.eval(expr)
        etor.env_restore(saved_env)
        return value
    
    def show(self, stream):
        show_elems(stream, self._exprs, '(', '; ', ')')

    def type_name(self):
        return 'Seq'
