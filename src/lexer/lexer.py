import lexer.char_stream

class Lexer:
    
    EOI = '#EOI#'

    def __init__(self):
        self._states = {}
        self._eoi_states = {}
        self._reserved_words = {}
        self._start_state_name = '#i'

    def add(self, state, chars, next_state, actions):
        try:
            for c in chars:
                self._add(state, c, next_state, actions)
        except TypeError:
            self._add(state, chars, next_state, actions)

    def _add(self, state_name, char, next_state, actions):
        #print('_addState adding', state_name, char, next_state, actions)
        state = self._states.get(state_name, {})
        self._states[state_name] = state # just in case .get returned a new dictionary
        state[char] = (next_state, actions)

    def save_pos(self):
        self._saved_pos = self._cs.get_pos()

    def get_saved_pos(self):
        return self._saved_pos

    def do_actions(self, actions, char):
        for action in actions:
            try:
                action(self, char)
            except TypeError:
                raise Exception('UFOSyntax.do_actions got unknown action: ' + repr(action))

    def eoi_state(self, state_name, actions):
        self._eoi_states[state_name] = actions

    def handle_state(self, c):
        state = self._states[self._state_name]
        self._state_name, actions = state.get(c, state.get(None))
        self.do_actions(actions, c)

    def lex(self, string):
        self._state_name = self._start_state_name
        self._word = ''
        self._tokens = []
        self._cs = lexer.char_stream.CharStream(string)
        self._saved_pos = self._cs.get_pos()
        for c in self._cs:
            self.handle_state(c)
        eoi_actions = self._eoi_states.get(self._state_name, None)
        if eoi_actions:
            for action in eoi_actions:
                action(self, None)
        else:
            if self._state_name != self._start_state_name:
                self.handle_state(None) # None = let the lexer know that the input stream is empty
        self.on_eoi()
        return self._tokens

    def on_eoi(self):
        self._tokens.append((Lexer.EOI, Lexer.EOI, self._cs.get_pos()))
