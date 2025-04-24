from alltypes.data.array import Array
import alltypes.data.binding
import alltypes.data.hashtable
import alltypes.data.list
import alltypes.data.queue
import alltypes.data.set
import alltypes.expr.assign
import alltypes.expr.identifier
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
    # expressions
    'Assign': alltypes.expr.assign.Assign.from_python_list,
    'Identifier': alltypes.expr.identifier.Identifier,
    # data structures
    'Array': Array.from_python_list,
    'Binding': alltypes.data.binding.Binding.from_python_list,
    'HashTable': alltypes.data.hashtable.HashTable.from_python_list,
    'List': alltypes.data.list.List.from_python_list,
    'Queue': alltypes.data.queue.Queue.from_python_list,
    'Set': alltypes.data.set.Set.from_python_list,
    # literals
    'Boolean': alltypes.literal.boolean.Boolean,
    'Float': alltypes.literal.float.Float,
    'Integer': alltypes.literal.integer.Integer,
    'Nil': alltypes.literal.nil.Nil,
    'String': alltypes.literal.string.String,
    'Symbol': alltypes.literal.symbol.Symbol
}
