from alltypes.data.array import Array
from alltypes.expr.assign import Assign
from alltypes.object import Object
from ufo_exception import UFOException

class Function (Object):
    
    class Rule:
        __slots__ = ('_params', '_body')

        def __init__(self, params, body):
            self._params = params
            self._body = body

        def closure(self, env):
            env_ctx = env.save()
            # pre-bind parameter identifiers to themselves
            for param in self._params:
                env.bind(param, param)
            # close the body
            closed_body = self._body.closure(env)
            env.restore(env_ctx)
            return Function.Rule(self._params, closed_body)
        
        def eval_body(self, etor):
            return self._body.eval(etor)

        @staticmethod
        def from_parser(parse_value):
            params = parse_value[0]
            body = parse_value[1]
            return Function.Rule(params, body)
        
        def matches(self, args, etor):
            binding_pairs = []
            if Array.pre_bind_elems(self._params, args, etor, binding_pairs):
                for (binding, value) in binding_pairs:
                    binding.rhs = value
                return True
            return False

        def show(self, stream):
            stream.write('(')
            first_iter = True
            for param in self._params:
                if first_iter:
                    first_iter = False
                else:
                    stream.write(', ')
                param.show(stream)
            stream.write(') = ')
            self._body.show(stream)

    class NamedFunction (Object):
        __slots__ = ('_name', '_rules')

        def __init__(self, name, rules):
            self._name = name
            self._rules = rules

        def eval_rec(self, etor):
            function = Function(self._rules)
            assign = Assign(self._name, function)
            return assign.eval(etor)

        def show(self, stream):
            stream.write('fun ')
            self._name.show(stream)
            Function.show_rules(self._function._rules)

    __slots__ = ('_rules')

    def __init__(self, rules):
        self._rules = rules

    def apply(self, args, etor):
        env = etor.env()
        env_save_point = env.save()
        for rule in self._rules:
            if rule.matches(args, env):
                value = rule.eval_body(etor)
                env.restore(env_save_point)
                return value
        env.restore(env_save_point)
        raise UFOException("No matching rule for arguments", arguments=args, function=self)

    @staticmethod
    def closure(rules, env):
        closed_rules = []
        for rule in rules:
            closed_rules.append(rule.closure(env))
        return Function(closed_rules)

    @staticmethod
    def from_parser(parse_value):
        name = parse_value[0]
        rules = [Function.Rule(rule[0], rule[1]) for rule in parse_value[1]]
        return Function(rules) if name is None else Function.NamedFunction(name, rules)

    def eval_rec(self, etor):
        return Function.closure(self._rules, etor.env())

    def show(self, stream):
        stream.write('fun ')
        Function.show_rules(stream, self._rules)

    @staticmethod
    def show_rules(stream, rules):
        first_iter = True
        for rule in rules:
            if first_iter:
                first_iter = False
            else:
                stream.write(' | ')
            rule.show(stream)

    def type_name(self):
        return 'Function'
