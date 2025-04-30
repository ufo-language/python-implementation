from alltypes.object import Object

class Quote (Object):

    __slots__ = ('_expr')

    def __init__(self, expr):
        self._expr = expr

    def eval_rec(self, etor):
        return self._expr

    def show(self, stream):
        stream.write('\'')
        self._expr.show(stream)
        stream.write('\'')

    def type_name(self):
        return 'Quote'
