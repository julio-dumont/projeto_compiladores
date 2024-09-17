from parser import Parser

def exibir_instrucoes():
    print("==== Calculadora de Expressões ====")
    print("Instruções de Uso:")
    print("1. Você pode usar operadores matemáticos (+, -, *, /).")
    print("2. Use parênteses para controlar a precedência, se necessário.")
    print("3. Você pode atribuir valores a variáveis usando o operador ':='.")
    print("4. Expressões com variáveis são permitidas e as variáveis podem ser reutilizadas.")
    print("\nExemplos:")
    print("   10 + 3 * (2 - 1)")
    print("   x := 10 + 3")
    print("   y := x / 2")
    print("   z := y + 5")
    print("   Resultado será calculado e exibido.\n")
    print("Digite 'sair' para encerrar o programa.")
    print("====================================\n")

if __name__ == '__main__':
    exibir_instrucoes()
    while True:
        code = input("Digite uma expressão: ")
        if code.lower() == 'sair':
            break
        parser = Parser(code)
        try:
            parser.parse()
        except Exception as e:
            print(f"Erro: {e}")
