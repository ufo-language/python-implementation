import lexer.char_stream
from lexer.lexer import *
from lexer.lexer_actions import *

def tokenize(input_string):
    lexer = UFOSyntax()
    tokens = lexer.lex(input_string)
    return tokens

class UFOSyntax (Lexer):

    def __init__(self):
        super().__init__()

        self._reserved_words = {
            'async', 'by', 'catch', 'cobegin', 'const', 'do', 'each',
            'else', 'end', 'false', 'for', 'foreach', 'forever', 'from',
            'fun', 'fn', 'if', 'in', 'let', 'letrec', 'loop', 'memoized',
            'macro', 'match', 'new', 'nondet', 'nil', 'struct', 'then',
            'times', 'to', 'true', 'try', 'typedef', 'until', 'while',
            'with'
        }
        self._true = 'true'
        self._false = 'false'

        # operator characters
        opers = '+-*/:.%^<>!#=?'

        # special characters
        # special = '()[]{};,'

        digit = '0123456789'
        hex_digit = 'abcdefABCDEF'
        upper_case = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        lower_case = 'abcdefghijklmnopqrstuvwxyz'

        self._start_state_name = '#i'

        self.add('#i', upper_case, '#sym',     [save_pos, keep_char])
        self.add('#i', lower_case, '#word',    [save_pos, keep_char])
        self.add('#i', '_',        '#word',    [save_pos, ignore_char])
        self.add('#i', '"',        '#string',  [save_pos, ignore_char])
        self.add('#i', digit,      '#number',  [save_pos, reuse_char])
        self.add('#i', '`',        '#ident',   [save_pos, ignore_char])
        self.add('#i', '|',        '#specSym', [save_pos, ignore_char])
        self.add('#i', '-',        '#dash',    [save_pos, keep_char])
        self.add('#i', opers,      '#oper',    [save_pos, keep_char])
        # self.add('#i', special,    '#i',       [save_pos, keep_char, special_char])
        self.add('#i', '/',        '#slash',   [save_pos, ignore_char])
        self.add('#i', ' \t',      '#i',       [ignore_char])
        self.add('#i', '\n',       '#i',       [ignore_char, eol])
        self.add('#i', None,       '#i',       [save_pos, keep_char, special_char])

        self.add('#number',    '0',        '#otherBase', [ignore_char])
        self.add('#number',    None,       '#int',       [reuse_char])

        self.add('#otherBase', 'bB',       '#binary',    [ignore_char])
        self.add('#otherBase', 'xX',       '#hex',       [ignore_char])
        self.add('#otherBase', None,       '#int',       [reuse_char])

        self.add('#binary',    '01',       '#binary',    [keep_char])
        self.add('#binary',    None,       '#i',         [reuse_char, create_binary_int])

        self.add('#hex',       digit,      '#hex',       [keep_char])
        self.add('#hex',       hex_digit,  '#hex',       [keep_char])
        self.add('#hex',       None,       '#i',         [reuse_char, create_hex_int])

        # block comment
        self.add('#commb1',    '*' ,       '#commb2',    [ignore_char])
        self.add('#commb1',    None,       '#commb1',    [ignore_char])

        self.add('#commb2',    '/',        '#i',         [ignore_char])
        self.add('#commb2',    None,       '#commb1',    [ignore_char])
        self.eof_state('#commb2', [err_unterm_comment])

        # line comment
        self.add('#comml',     '/n',       '#i',         [ignore_char, eol])
        self.add('#comml',     None,       '#comml',     [ignore_char])

        self.add('#dash',      digit,      '#int',       [keep_char])
        self.add('#dash',      opers,      '#oper',      [keep_char])
        self.add('#dash',      '-',        '#dash',      [keep_char])
        self.add('#dash',      None,       '#i',         [reuse_char, create_oper])

        self.add('#float',     digit,      '#float',     [keep_char])
        self.add('#float',     None,       '#i',         [reuse_char, create_float])

        self.add('#ident',     '`',        '#i',         [ignore_char, create_word])
        self.add('#ident',     None,       '#ident',     [keep_char])
        self.eof_state('#ident', [err_unterm_backquote])

        self.add('#int',       digit,      '#int',       [keep_char])
        self.add('#int',       '.',        '#float',     [keep_char])
        self.add('#int',       None,       '#i',         [reuse_char, create_int])

        self.add('#oper',      opers,      '#oper',      [keep_char])
        self.add('#oper',      '-',        '#oper',      [keep_char])
        self.add('#oper',      '=',        '#oper',      [keep_char])
        self.add('#oper',      None,       '#i',         [reuse_char, create_oper])

        self.add('#slash',     '/',        '#comml',     [ignore_char]) # line comment
        self.add('#slash',     '*',        '#commb1',    [ignore_char]) # block comment
        self.add('#slash',     None,       '#oper',      [inject('/'), reuse_char])

        self.add('#string',    '\n',       '#i',         [err_unterm_string])
        self.add('#string',    None,       '#string',    [keep_char])
        self.add('#string',    '"',        '#i',         [ignore_char, create_string])
        self.eof_state('#string', [err_unterm_string])

        # special symbol
        self.add('#specSym',   '|',        '#i',         [ignore_char, create_symbol])
        self.add('#specSym',   None,       '#specSym',   [keep_char])
        self.eof_state('#specSym', [err_unterm_bar])

        self.add('#sym',       upper_case,  '#sym',       [keep_char])
        self.add('#sym',       lower_case,  '#sym',       [keep_char])
        self.add('#sym',       digit,      '#sym',       [keep_char])
        self.add('#sym',       '_?',       '#sym',       [keep_char])
        self.add('#sym',       None,       '#i',         [reuse_char, create_symbol])

        self.add('#word',      upper_case,  '#word',      [keep_char])
        self.add('#word',      lower_case,  '#word',      [keep_char])
        self.add('#word',      digit,      '#word',      [keep_char])
        self.add('#word',      '_?',       '#word',      [keep_char])
        self.add('#word',      None,       '#i',         [reuse_char, create_word])  # create_word checks for 'true' and 'false'
