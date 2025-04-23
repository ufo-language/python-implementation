import alltypes.data.array
import alltypes.data.list
import alltypes.literal.float
import alltypes.literal.integer
import alltypes.literal.string
import alltypes.literal.symbol

def builder(type_name, *args, **kwargs):
    fun = BUILDERS.get(type_name)
    if fun is None:
        raise Exception(f"ufo_object_builders.builder type_name '{type_name}' not found")
    return fun(*args, **kwargs)

BUILDERS = {
    # literals
    'Float': alltypes.literal.float.Float,
    'Integer': alltypes.literal.integer.Integer,
    'String': alltypes.literal.string.String,
    'Symbol': alltypes.literal.symbol.Symbol,
    # data structures
    'Array': alltypes.data.list.Array,
    'List': alltypes.data.list.List,
    # expressions
}
