class ParserState:

    __slots__ = (
        'parser_table', 'object_builder', 'tokens', 'index', 'value',
        'memo_table', 'memo_key', 'saved_ctx', 'most_recent_parser_name'
    )

    def __init__(self, parser_table, object_builder, tokens):
        self.parser_table = parser_table
        self.object_builder = object_builder
        self.tokens = tokens
        self.index = 0
        self.value = None
        self.memo_table = {}
        self.memo_key = None
        self.saved_ctx = []
        self.most_recent_parser_name = None

    def current_token(self):
        return self.tokens[self.index]

    def advance(self, n=1):
        # print(f"{indent()}advance from", self.index, "to", self.index + n)
        self.index += n

    def next_token(self):
        return self.tokens[self.index]

    # def apply(self, fun):
    #     self.value = fun(self.value)

    def get_ctx(self):
        return (self.index, self.value)

    def set_ctx(self, ctx):
        #print("set_ctx", ctx)
        (self.index, self.value) = ctx
