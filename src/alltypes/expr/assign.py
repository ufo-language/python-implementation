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
        env = etor.env()
        print("assign.eval_rec 1 env=", env)
        saved_env_ctx = env.save()
        value = etor.eval(self._rhs)
        if self._lhs.match(value, env):
            print("assign.eval_rec 2 env=", env)
            return value
        env.restore(saved_env_ctx)
        raise UFOException("Structure mismatch", lhs=self._lhs, rhs=self._rhs)

    def show(self, stream):
        self._lhs.show(stream)
        stream.write(' := ')
        self._rhs.show(stream)

    def type_name(self):
        return 'Assignment'
