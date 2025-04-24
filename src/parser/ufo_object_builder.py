import alltypes.data.array
import alltypes.data.list
import alltypes.data.queue
import alltypes.literal.boolean
import alltypes.literal.float
import alltypes.literal.integer
import alltypes.literal.nil
import alltypes.literal.string
import alltypes.literal.symbol

def builder(type_name, *args, **kwargs):
    fun = BUILDERS.get(type_name)
    if fun is None:
        raise Exception(f"ufo_object_builder.builder type_name '{type_name}' not found")
    return fun(*args, **kwargs)

BUILDERS = {
    # literals
    'Boolean': alltypes.literal.boolean.Boolean,
    'Float': alltypes.literal.float.Float,
    'Integer': alltypes.literal.integer.Integer,
    'Nil': alltypes.literal.nil.Nil,
    'String': alltypes.literal.string.String,
    'Symbol': alltypes.literal.symbol.Symbol,
    # data structures
    'Array': alltypes.data.array.Array,
    'List': alltypes.data.list.List.from_python_list,
    'Queue': alltypes.data.queue.Queue.from_python_list,
    # expressions
}
