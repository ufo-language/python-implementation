from alltypes.object import Object

class Function (Object):

    class Rule:
        __slots__ = ('params', 'body')

        def __init__(self, params, body):
            self.params = params
            self.body = body

        @staticmethod
        def from_parser(parse_value):
            params = parse_value[0]
            body = parse_value[1]
            return Function.Rule(params, body)

        def __repr__(self):
            return '(' + ', '.join([repr(param) for param in self.params]) + ') = ' + repr(self.body)

    __slots__ = ('_name', '_rules')

    def __init__(self, name, rules):
        self._name = name
        self._rules = rules

    @staticmethod
    def from_parser(parse_value):
        name = parse_value[0]
        rules = []
        for rule in parse_value[1]:
            rules.append(Function.Rule(rule[0], rule[1]))
        value = Function(name, rules)
        print("Function.from_parser returning value", value)
        return value

    def eval_rec(self, etor):
        # TODO create and return a closure
        assert False

    def type_name(self):
        return 'Function'

    def __repr__(self):
        return 'fun ' + (repr(self._name) if self._name is not None else '') + ' | '.join([repr(rule) for rule in self._rules])
