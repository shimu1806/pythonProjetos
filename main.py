# Binary-to-Decimal number converter

"""

para converter um numero binario em decimal é necessário realizar uma operação de todos
algoritimos, partindo da última posição, que se baseia em, na base 2, a última posição representa
0 e será a potencia, após isso, o próximo algoritimo, que será a penúltima posição, representará
o valor 1, e assim segue. após ter o resultado de todas as bases, é realizado a soma, que resultará
no valor decimal 

"""

binario = int(input("Digita a porra do numerio binario, verme: ")) 
n = len(str(binario)) # servirá para reduzir o comprimento do número binario, podendo realizar a operação de todas as posições
valorDigitado = binario # servirá pra exibir o resultado
decimal = 0 # como o decimal começa a partir do 0, 0
i = 0 # a base começa sendo elevada a 0, portanto, a variavel i, que representa o espoente é 0 

while n >= 0: # o ciclo encerra quando o binario for totalmente operado
        resto = binario % 10 
        print("o resto deu: ", resto)
        decimal = decimal + (resto * (2**i)) # o decimal vai aumentando conforme o programa operta, no caso, ele está recebendo o valor da base 2** ao esponte que cresce conforme o ciclo gira + o resto da divisão do número binário
        print("o decimal ta indo em: ", decimal)
        n = n - 1 # o comprimento vai reduzindo conforme segue o ciclo
        print("o n ta indo em: ", n)
        i = i + 1 # o esponte vai aumentando conforme segue o ciclo
        print("o i ta indo em: ", i)
        binario = binario // 10 # binario vai reduzindo conforme segue o ciclo
        print("o binario ta indo em: ",binario)
        
print("o binario que tu digitou deu: {}\ne ele converta para {} em decimal".format(valorDigitado,decimal))