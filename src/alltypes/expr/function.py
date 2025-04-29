from alltypes.expr.assign import Assign
from alltypes.object import Object

class Function (Object):
    
    class Rule:
        __slots__ = ('_params', '_body')

        def __init__(self, params, body):
            self._params = params
            self._body = body

        def closure(self, env):
            # print("Rule.closure self=", self)
            env_ctx = env.save()
            # pre-bind parameter identifiers to themselves
            for param in self._params:
                env.bind(param, param)
            # close the body
            closed_body = self._body.closure(env)
            env.restore(env_ctx)
            return Function.Rule(self._params, closed_body)

        @staticmethod
        def from_parser(parse_value):
            params = parse_value[0]
            body = parse_value[1]
            return Function.Rule(params, body)

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
            etor.bind(self._name, self._name)
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
        # print("Function.__init__ rules =", rules)

    @staticmethod
    def closure(rules, env):
        # print("Function.closure called", len(rules), "rules =", rules)
        closed_rules = []
        for rule in rules:
            closed_rules.append(rule.closure(env))
            # print("Function.closure rules =", rules)
        return Function(closed_rules)

    @staticmethod
    def from_parser(parse_value):
        name = parse_value[0]
        rules = [Function.Rule(rule[0], rule[1]) for rule in parse_value[1]]
        return Function(rules) if name is None else Function.NamedFunction(name, rules)

    def eval_rec(self, etor):
        # print("Function.eval_rec called")
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
