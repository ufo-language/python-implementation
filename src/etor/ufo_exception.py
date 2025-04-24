class UFOException (Exception):

    __slots__ = ('_args', '_kwargs')

    def __init__(self, *args, **kwargs):
        self._args = args
        self._kwargs = kwargs

    def __repr__(self):
        return str(args) + ' ' + str(kwargs)
