import lexer.ufo_syntax
import parser.parser
import parser.ufo_grammar
import parser.ufo_object_builder

def parse_string(input_string):
    # print(f"ufo_parser.parse input_string = '{input_string}'")
    tokens = lexer.ufo_syntax.tokenize(input_string)
    return parse_tokens(tokens)

def parse_tokens(tokens):
    # print(f"ufo_parser.parse tokens = '{tokens}'")
    parser_table = parser.ufo_grammar.PARSER_TABLE
    object_builder = parser.ufo_object_builder.builder
    parse_result = parser.parser.parse_entry_point('Any', parser_table, object_builder, tokens)
    # print("ufo_parser.parse_tokens got result", parse_result)
    return parse_result
