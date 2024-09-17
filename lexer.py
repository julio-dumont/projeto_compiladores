import re

class Tokenizer:
    def __init__(self, code):
        self.code = code
        self.tokens = self.tokenize()
        self.pos = 0

    def tokenize(self):
        token_spec = [
            ('NUMBER', r'\d+(\.\d*)?'),  # Números inteiros ou reais
            ('ASSIGN', r':='),           # Atribuição
            ('ID', r'[a-zA-Z_]\w*'),     # Identificadores (variáveis)
            ('PLUS', r'\+'),             # Operador +
            ('MINUS', r'-'),             # Operador -
            ('TIMES', r'\*'),            # Operador *
            ('DIVIDE', r'/'),            # Operador /
            ('LPAREN', r'\('),           # Parêntese esquerdo
            ('RPAREN', r'\)'),           # Parêntese direito
            ('SKIP', r'[ \t]+'),         # Espaços em branco
            ('MISMATCH', r'.')           # Caracteres inválidos
        ]
        token_regex = '|'.join(f'(?P<{name}>{regex})' for name, regex in token_spec)
        scanner = re.finditer(token_regex, self.code)
        tokens = []
        for match in scanner:
            kind = match.lastgroup
            value = match.group(kind)
            if kind == 'NUMBER':
                value = float(value)
            if kind == 'SKIP':
                continue
            elif kind == 'MISMATCH':
                raise SyntaxError(f'Caractere inesperado: {value}')
            tokens.append((kind, value))
        return tokens

    def next_token(self):
        if self.pos < len(self.tokens):
            token = self.tokens[self.pos]
            self.pos += 1
            return token
        return None

    def peek(self):
        if self.pos < len(self.tokens):
            return self.tokens[self.pos]
        return None
