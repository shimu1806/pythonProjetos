"""

Calculadora simples que realiza operações básicas

"""

print("Calculadora em .Py\n\n\n")

Numero1 = int(input("Digite o primeiro valor: "))
operador = (input(
    "\nDigite um operador entre \n+ soma,\n- subtração,\n* multiplicação,\n/ divisão,\n// divisão inteira,\n% módulo,\n** expoente :\n "))
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
elif operador == "//":
    Resultado = Numero1 // Numero2
    print("\nA divisão inteira dos valor resulta: ", Resultado)
elif operador == "%":
    Resultado = Numero1 % Numero2
    print("\nO módulo (resto da divisão) dos valor resulta: ", Resultado)
elif operador == "**":
    Resultado = Numero1 ** Numero2
    print("\nA exponenciação dos valor resulta: ", Resultado)
else:   
    print("\nOperador inválido...")
