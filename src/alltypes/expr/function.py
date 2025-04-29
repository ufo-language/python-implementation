from alltypes.object import Object

class Function (Object):
    
    class Rule:
        __slots__ = ('params', 'body')

        def __init__(self, params, body):
            self.params = params
            self.body = body

        def closure(self, env):
            env_ctx = env.save()
            # pre-bind parameter identifiers to themselves
            for param in self.params:
                env.bind(param, param)
            # close the body
            closed_body = self.body.closure(env)
            env.restore(env_ctx)
            return Function.Rule(self.params, closed_body)

        @staticmethod
        def from_parser(parse_value):
            params = parse_value[0]
            body = parse_value[1]
            return Function.Rule(params, body)

        def show(self, stream):
            stream.write('(')
            first_iter = True
            for param in self.params:
                if first_iter:
                    first_iter = False
                else:
                    stream.write(', ')
                param.show(stream)
            stream.write(') = ')
            self.body.show(stream)

    class NamedFunction:
        __slots__ = ('name', 'function')

        def __init__(self, name, function):
            self.name = name
            self.function = function

        def eval_rec(self, etor):
            etor.bind(self._name, self._name)
            closure = self.function.eval(etor)
            etor.rebind(self._name, closure)
            return closure

        def show(self, stream):
            stream.write('fun ')
            self._name.show(stream)
            Function.show_rules(self.rules)

    __slots__ = ('_rules')

    def __init__(self, rules):
        self._rules = rules

    @staticmethod
    def closure(rules, env):
        rules = []
        for rule in rules:
            rules.append(rule.closure(env))
        return Function(rules)

    @staticmethod
    def from_parser(parse_value):
        name = parse_value[0]
        rules = []
        for rule in parse_value[1]:
            rules.append(Function.Rule(rule[0], rule[1]))
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
