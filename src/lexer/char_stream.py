class CharStream:

    __slots__ = ('_string', '_name', '_line', '_col', '_pos', '_len', '_saved_newlines')

    def __init__(self, string, name=None):
        self._string = string
        self._name = name
        self._line = 1
        self._col = 0
        self._pos = 0
        self._len = len(string)
        self._saved_newlines = []

    def get_pos(self):
        return (self._name, self._line, self._col, self._pos)

    def __iter__(self):
        return self

    def __next__(self):
        if self._pos == self._len:
            raise StopIteration
        c = self._string[self._pos]
        self._pos += 1
        self._col += 1
        if c == '\n':
            self._saved_newlines.append(self._col - 1)
            self._line += 1
            self._col = 0
        return c

    def unget(self):
        if self._pos > 0:
            self._pos -= 1
            self._col -= 1
            if self._string[self._pos] == '\n':
                self._line -= 1
                self._col = self._saved_newlines.pop()
