from alltypes.literal.nil import Nil
from alltypes.object import Object

class IfThen (Object):

    __slots__ = ('_cond', '_conseq', '_alt')

    def __init__(self, cond, conseq, alt=None):
        self._cond = cond
        self._conseq = conseq
        self._alt = alt if alt is not None else Nil()

    @staticmethod
    def from_parser(parse_value):
        return IfThen(*parse_value)

    def eval_rec(self, etor):
        cond_val = etor.eval(self._cond)
        if cond_val.bool_value():
            return etor.eval(self._conseq)
        return etor.eval(self._alt)
    
    def show(self, stream):
        stream.write('if ')
        self._cond.show(stream)
        stream.write(' then ')
        self._conseq.show(stream)
        if self._alt is not None:
            self._alt.show(stream)

    def type_name(self):
        return 'If'
