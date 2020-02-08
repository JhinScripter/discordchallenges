#Calculadora simples sem Interface com as funções de "somar, subtrair, multiplicar e dividir".

numero1 = int(input("Primeiro número: "))
numero2 = int(input("Segundo número: "))
operacao = input("Operação: ")
if operacao == "+":
    print(numero1, operacao, numero2, "=", numero1 + numero2)
elif operacao == "-":
    print(numero1, operacao, numero2, "=", numero1 - numero2)
elif operacao == "x":
    print(numero1, operacao, numero2, "=", numero1 * numero2)
elif operacao == ":":
    print(numero1, operacao, numero2, "=", numero1 / numero2)
else:
    print("ERRO NA OPERAÇÃO! (TENTE: [+ | - | x | :])")