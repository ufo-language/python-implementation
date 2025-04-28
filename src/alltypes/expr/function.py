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

    __slots__ = ('_name', '_rules')

    def __init__(self, name, rules):
        self._name = name
        self._rules = rules

    def closure(self, env):
        rules = []
        for rule in self._rules:
            rules.append(rule.closure(env))
        return Function(self._name, rules)

    @staticmethod
    def from_parser(parse_value):
        name = parse_value[0]
        rules = []
        for rule in parse_value[1]:
            rules.append(Function.Rule(rule[0], rule[1]))
        return Function(name, rules)

    def eval_rec(self, etor):
        if self._name is not None:
            etor.bind(self._name, self._name)
        closure = self.closure(etor.env())
        if self._name is not None:
            etor.rebind(self._name, closure)
        return closure

    def show(self, stream):
        stream.write('fun ')
        if self._name is not None:
            self._name.show(stream)
        first_iter = True
        for rule in self._rules:
            if first_iter:
                first_iter = False
            else:
                stream.write(' | ')
            rule.show(stream)

    def type_name(self):
        return 'Function'
