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
            return Array.match_elems(self._params, args, etor)

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
        __slots__ = ('_name', '_rules', '_is_macro')

        def __init__(self, name, rules, is_macro):
            self._name = name
            self._rules = rules
            self._is_macro = is_macro

        def eval_rec(self, etor):
            function = Function(self._rules, self._is_macro)
            assign = Assign(self._name, function)
            return assign.eval(etor)

        def show(self, stream):
            stream.write('fun ')
            self._name.show(stream)
            Function.show_rules(self._function._rules)

    __slots__ = ('_rules', '_is_macro')

    def __init__(self, rules, is_macro):
        self._rules = rules
        self._is_macro = is_macro

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
    def closure(rules, is_macro, env):
        closed_rules = []
        for rule in rules:
            closed_rules.append(rule.closure(env))
        return Function(closed_rules, is_macro)

    @staticmethod
    def from_parser(parse_value):
        print("Function.from_parser value=", parse_value)
        is_macro = parse_value[0]
        name = parse_value[1]
        rules = [Function.Rule(rule[0], rule[1]) for rule in parse_value[2]]
        return Function(rules, is_macro) if name is None else Function.NamedFunction(name, rules, is_macro)

    def eval_rec(self, etor):
        return Function.closure(self._rules, self._is_macro, etor.env())
    
    def is_macro(self):
        return self._is_macro

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
