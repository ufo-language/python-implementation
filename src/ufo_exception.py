class UFOException (Exception):

    # don't bother with __slots__ because Exception already has a __dict__

    def __init__(self, message, *args, **kwargs):
        self.message = message
        self.args = args
        self.kwargs = kwargs

    def __repr__(self):
        return self.message + '\n' + repr(self.args) + ' ' + repr(self.kwargs)

    def __str__(self):
        return self.__repr__()
