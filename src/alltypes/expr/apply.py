from alltypes.data._show_elems import show_elems
from alltypes.expr.identifier import Identifier
from alltypes.object import Object

class Apply (Object):

    __slots__ = ('_callee', '_args')

    def __init__(self, callee, args):
        self._callee = callee
        self._args = args

    @staticmethod
    def from_parser(parser_value):
        app = Apply(*parser_value)
        return app

    def eval_rec(self, etor):
        evaled_callee = etor.eval(self._callee)
        if evaled_callee.is_macro():
            evaled_args = self._args
        else:
            evaled_args = [arg.eval(etor) for arg in self._args]
        return evaled_callee.apply(evaled_args, etor)

    def show(self, stream):
        if isinstance(self._callee, Identifier):
            self._callee.show(stream)
        else:
            stream.write('(')
            self._callee.show(stream)
            stream.write(')')
        show_elems(stream, self._args, '(', ', ', ')')

    def type_name(self):
        return 'Application'
