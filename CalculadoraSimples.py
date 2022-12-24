"""

Calculadora simples que realiza operações básicas

"""

print("TOP 10 AS MAIS TOPS E EFICIENTES CALCULADORAS OFF THE MUNDO\n\n\n")

Numero1 = int(input("Digite o primeiro valor: "))
operador = (input("\nDigite um operador entre (+:, -, *, / : "))
Numero2 = int(input("\nDigite o segundo valor: "))
Resultado = 0

if operador == "+":
    Resultado = Numero1 + Numero2
    print("\nA soma dos valor resulta: ", Resultado)
elif operador == "-":
    Resultado = Numero1 - Numero2
    print("\nA subtração dos valor resulta: ", Resultado)
elif operador == "*":
    Resultado = Numero1 * Numero2
    print("\nA multiplicação dos valor resulta: ", Resultado)
elif operador == "/":
    Resultado = Numero1 / Numero2
    print("\nA divisão dos valor resulta: ", Resultado)
else:   
    print("\nOperador inválido...")
