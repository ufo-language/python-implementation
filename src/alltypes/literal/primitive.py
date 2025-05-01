from alltypes.data.hashtable import HashTable
from alltypes.expr.identifier import Identifier
from alltypes.object import Object
from etor.environment import Environment
from ufo_exception import UFOException

class Primitive (Object):
    
    ALL_PRIMS = {}

    __slots__ = ('_name', '_param_rules', '_is_macro')

    def __init__(self, name, param_rules=((),), is_macro=False):
        self._name = name
        self._param_rules = param_rules
        self._is_macro = is_macro

    def apply(self, args, etor):
        ''' Do not override. Override apply_aux instead. '''
        param_rule_num = self.check_arg_types(args)
        return self.apply_aux(args, param_rule_num, etor)
    
    def apply_aux(self, args, param_rule_num, etor):
        ''' Subclasses should override. '''
        pass
    
    def check_param_type(self, arg, param_type):
        arg_type = type(arg)
        if type(param_type) is tuple:
            for type_elem in param_type:
                if type_elem is arg_type:
                    return True
            return False
        return param_type is object or type(arg) is param_type

    def check_rule(self, args, rule):
        n_args = len(args)
        if len(rule) != n_args:
            return False
        for (arg, param_type) in zip(args, rule):
            if not self.check_param_type(arg, param_type):
                return False
        return True

    def check_arg_types(self, args):
        n_args = len(args)
        for (rule_num, param_rule) in enumerate(self._param_rules):
            if self.check_rule(args, param_rule):
                return rule_num
        raise UFOException("Argument type mismatch", args=args, param_types=self._param_rules)

    def define_prim(self, ns, ns_name=''):
        if type(ns) is HashTable:
            full_name = ns_name + '_' + self._name
            Primitive.ALL_PRIMS[full_name] = self
            ns[Identifier(self._name)] = self
        elif type(ns) is Environment:
            Primitive.ALL_PRIMS[self._name] = self
            ns.bind(Identifier(self._name), self)

    def __hash__(self):
        return hash(self._function)
    
    def is_macro(self):
        return self._is_macro

    def __lt__(self, other):
        if not isinstance(other, Primitive):
            return repr(self) < repr(other)
        return self._function < other._function

    def show(self, stream):
        stream.write('Primitive{')
        stream.write(self._name)
        stream.write('}')

    def type_name(self):
        return 'Primitive'
