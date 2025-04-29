from alltypes.data._show_elems import show_elems
from alltypes.expr.identifier import Identifier
from alltypes.object import Object

class Apply (Object):

    __slots__ = ('_abstr', '_args')

    def __init__(self, abstr, args):
        self._abstr = abstr
        self._args = args

    @staticmethod
    def from_parser(parser_value):
        app = Apply(*parser_value)
        return app

    def eval_rec(self, etor):
        evaled_abstr = etor.eval(self._abstr)
        evaled_args = [arg.eval(etor) for arg in self._args]
        print("Apply.eval_rec abstr =", evaled_abstr)
        print("Apply.eval_rec args =", evaled_args)
        return self

    def show(self, stream):
        if isinstance(self._abstr, Identifier):
            self._abstr.show(stream)
        else:
            stream.write('(')
            self._abstr.show(stream)
            stream.write(')')
        show_elems(stream, self._args, '(', ', ', ')')

    def type_name(self):
        return 'Application'
