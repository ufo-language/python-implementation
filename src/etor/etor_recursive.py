from etor._etor import Evaluator
import etor.environment

class EtorRecursive (Evaluator):

    __slots__ = ('_env',)

    def __init__(self):
        self.type = 'RECURSIVE'
        self._env = etor.environment.Environment()

    def bind(self, ident, value):
        self._env.bind(ident, value)

    def eval(self, expr):
        return expr.eval_rec(self)

    def lookup(self, identifier):
        return self._env.lookup(identifier)

    def match_bind(self, lhs, rhs):
        env_save_point = self._env.save()
        bindings = lhs.match(rhs, self._env)
        if bindings is None:
            self._env.restore(env_save_point)
            return False
        return True
