from etor._etor import Evaluator
import etor.environment

class EtorRecursive (Evaluator):

    __slots__ = ('_env',)

    def __init__(self):
        self.type = 'RECURSIVE'
        self._env = etor.environment.Environment()

    def bind(self, ident, value):
        self._env.bind(ident, value)

    def env(self):
        return self._env

    def env_save(self):
        return self._env.save()
    
    def env_restore(self, ctx):
        self._env.restore(ctx)

    def eval(self, expr):
        return expr.eval_rec(self)
    
    def get_env_rel(self, index):
        return self._env.locate_binding_abs

    def lookup(self, identifier):
        return self._env.lookup(identifier)
