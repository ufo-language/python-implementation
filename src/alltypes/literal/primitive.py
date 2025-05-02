import inspect

from alltypes.data.array import Array
from alltypes.data.hashtable import HashTable
from alltypes.data.list import List
from alltypes.data.term import Term
from alltypes.expr.binop import BinOp
from alltypes.expr.identifier import Identifier
from alltypes.literal.symbol import Symbol
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

    def about(self):
        if self.__doc__ is not None:
            return self.__doc__.strip()
        return "No information available."

    def apply(self, args, etor):
        ''' Do not override. Override apply_aux instead. '''
        param_rule_num = self.check_arg_types(args)
        return self.apply_aux(args, param_rule_num, etor)
    
    def apply_aux(self, args, param_rule_num, etor):
        ''' Subclasses should override. '''
        pass
    
    def check_param_type(self, arg, param_type):
        if inspect.isclass(param_type) and issubclass(param_type, Object):
            return isinstance(arg, param_type)
        if type(param_type) is tuple:
            for type_elem in param_type:
                if self.check_param_type(arg, type_elem):
                    return True
            return False
        if hasattr(param_type, 'term_name') and callable(param_type):
            return param_type(arg)
        if param_type is object:
            return True
        return False

    def check_rule(self, args, rule):
        n_args = len(args)
        if len(rule) != n_args:
            return False
        for (arg, param_type) in zip(args, rule):
            if not self.check_param_type(arg, param_type):
                return False
        return True
    
    def param_rules(self):
        return self._param_rules
    
    @staticmethod
    def param_type_demangle(param_type):
        if param_type is object:
            return Symbol('Any')
        if hasattr(param_type, 'term_name'):
            return param_type.term_name
        if hasattr(param_type, '__name__'):
            return Symbol(param_type.__name__)
        if type(param_type) is tuple:
            return List.create([Primitive.param_type_demangle(elem) for elem in param_type])
        raise SystemError(f"Unhandled param_type {param_type} :: {type(param_type)}")

    @staticmethod
    def param_rule_demangle(param_rule):
        return Array.create([Primitive.param_type_demangle(elem) for elem in param_rule])

    @staticmethod
    def param_rules_demangle(param_rules):
        demangled_rules = [Primitive.param_rule_demangle(rule) for rule in param_rules]
        if len(demangled_rules) == 1:
            return demangled_rules[0]
        return List.create([Primitive.param_rule_demangle(rule) for rule in param_rules])

    def check_arg_types(self, args):
        n_args = len(args)
        for (rule_num, param_rule) in enumerate(self._param_rules):
            if self.check_rule(args, param_rule):
                return rule_num
        param_types = Primitive.param_rules_demangle(self._param_rules)
        oper = Identifier('::')
        arg_array = Array.create([BinOp(arg, oper, Symbol(arg.type_name())) for arg in args])
        raise UFOException("Argument type mismatch", prim=self, param_types=param_types, args=arg_array)

    def define_prim(self, ns, ns_name=''):
        if type(ns) is HashTable:
            full_name = ns_name + '_' + self._name
            Primitive.ALL_PRIMS[full_name] = self
            ns[Identifier(self._name)] = self
            self._name = full_name
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

    @staticmethod
    def term_type(name):
        symbol = Symbol(name)
        def fun(term):
            return type(term) == Term and term.name() is symbol
        fun.term_name = symbol
        return fun

    def type_name(self):
        return 'Primitive'
