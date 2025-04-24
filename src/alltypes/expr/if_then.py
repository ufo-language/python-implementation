import alltypes.literal.nil
from alltypes.object import Object

class If (Object):

    __slots__ = ('_cond', '_conseq', '_alt')

    def __init__(self, cond, conseq, alt):
        self._cond = cond
        self._conseq = conseq
        self._alt = alt

    @staticmethod
    def from_python_list(python_list):
        return If(*python_list)

    def eval_rec(self, etor):
        cond_val = etor.eval(self._cond)
        if cond_val.bool_value():
            return etor.eval(self._conseq)
        return etor.eval(self._alt)

    def type_name(self):
        return 'If'

    def __repr__(self):
        return f"if {self._cond} then {self._conseq} else {self._alt}"
