from alltypes.literal.nil import Nil
from alltypes.object import Object
from ufo_exception import UFOException

class Assign (Object):

    __slots__ = ('_lhs', '_rhs')

    def __init__(self, lhs, rhs):
        self._lhs = lhs
        self._rhs = rhs

    @staticmethod
    def from_parser(parser_value):
        return Assign(*parser_value)

    def eval_rec(self, etor):
        saved_env_ctx = etor.env_save()
        binding_pairs = []
        if self._lhs.pre_bind(self._rhs, etor.env(), binding_pairs):
            for (binding, expr) in binding_pairs:
                value = expr.eval(etor)
                binding.rhs = value
            return Nil()
        etor.env_restore(saved_env_ctx)
        raise UFOException("Structure mismatch", lhs=self._lhs, rhs=self._rhs)

    def show(self, stream):
        self._lhs.show(stream)
        stream.write(' := ')
        self._rhs.show(stream)

    def type_name(self):
        return 'Assignment'
