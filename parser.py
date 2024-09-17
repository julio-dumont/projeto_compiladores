from lexer import Tokenizer

class Parser:
    def __init__(self, code):
        self.tokenizer = Tokenizer(code)
        self.current_token = self.tokenizer.next_token()
        self.variables = {}

    def consume(self, token_type):
        if self.current_token and self.current_token[0] == token_type:
            self.current_token = self.tokenizer.next_token()
        else:
            raise SyntaxError(f'Esperado {token_type}, encontrado {self.current_token}')

    def parse(self):
        while self.current_token is not None:
            self.cmd_expr()

    def cmd_expr(self):
        if self.current_token[0] == 'ID':
            var_name = self.current_token[1]
            self.consume('ID')
            self.consume('ASSIGN')
            result = self.expr()
            self.variables[var_name] = result
            print(f'{var_name} := {result}')
        else:
            result = self.expr()
            print(f'Resultado: {result}')

    def expr(self):
        result = self.term()
        while self.current_token and self.current_token[0] in ('PLUS', 'MINUS'):
            if self.current_token[0] == 'PLUS':
                self.consume('PLUS')
                result += self.term()
            elif self.current_token[0] == 'MINUS':
                self.consume('MINUS')
                result -= self.term()
        return result

    def term(self):
        result = self.factor()
        while self.current_token and self.current_token[0] in ('TIMES', 'DIVIDE'):
            if self.current_token[0] == 'TIMES':
                self.consume('TIMES')
                result *= self.factor()
            elif self.current_token[0] == 'DIVIDE':
                self.consume('DIVIDE')
                result /= self.factor()
        return result

    def factor(self):
        token = self.current_token
        if token[0] == 'NUMBER':
            self.consume('NUMBER')
            return token[1]
        elif token[0] == 'ID':
            var_name = token[1]
            if var_name in self.variables:
                self.consume('ID')
                return self.variables[var_name]
            else:
                raise NameError(f'Variável não definida: {var_name}')
        elif token[0] == 'LPAREN':
            self.consume('LPAREN')
            result = self.expr()
            self.consume('RPAREN')
            return result
        else:
            raise SyntaxError(f'Erro de sintaxe: {token}')
