# These are constructors for the specific types in the language

class ObjectBuilder:

    def __init__(self):
        self._constructors = {}

    def define(name, constructor):
        self._constructors[name] = constructor

    def create(name, *args, **kwargs):
        constructor = self._constructors.get(name)
        if constructor is None:
            throw Exception(f"ObjectBuilder: no constructor for '{name}'")
        constructor(*args, **kwargs)
