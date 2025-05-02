class UFOException (Exception):

    # don't bother with __slots__ because Exception already has a __dict__

    def __init__(self, message, *args, **kwargs):
        self.message = message
        self.args = args
        self.kwargs = kwargs

    def __repr__(self):
        if self.kwargs:
            return self.message + '\n' + '\n'.join((f"  {key}={value}" for (key, value) in self.kwargs.items()))
        return self.message

    def __str__(self):
        return self.__repr__()
