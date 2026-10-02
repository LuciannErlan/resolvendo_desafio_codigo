#Operações matemáticas básicas
n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
operacao = input("Digite a operação desejada (+, -, *, /): ")

if operacao == '+':
    print(f"Adição: {n1 + n2}")
elif operacao == '-':
    print(f"Subtração: {abs(n1 - n2)}")
elif operacao == '*':
    print(f"Multiplicação: {n1 * n2}")  
elif operacao == '/':
    if n2 != 0:
        print(f"Divisão: {n1 / n2}")
else:
        print("Erro: Operação inválida.")

print("Fim do programa.")