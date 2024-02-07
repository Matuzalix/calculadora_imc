import os

print("-"*30)
print("Bem vindos a nossa calculadora")
print("-"*30)

print("Escolha a operação desejada na lista abaixo:")

print("0 = Soma")
print("1 = Subtração")
print("2 = Multiplicação")
print("3 = Divisão")
print("4 = Exponencial")

operador = float(input("Digite a operação escolhida: "))

while True:
    if operador == 0:
        n1 = float(input("digite o primeiro número: "))
        n2 = float(input("digite o segundo número: "))
        resultado = n1 + n2
        print(resultado)
    elif operador == 1:
        n1 = float(input("digite o primeiro número: "))
        n2 = float(input("digite o segundo número: "))
        resultado = n1 - n2
        print(resultado)
    elif operador == 2:
        n1 = float(input("digite o primeiro número: "))
        n2 = float(input("digite o segundo número: "))
        resultado = n1 * n2
        print(resultado)
    elif operador == 3:
        n1 = float(input("digite o primeiro número: "))
        n2 = float(input("digite o segundo número: "))
        resultado = n1 / n2
        print(resultado)
    elif operador == 4:
        n1 = float(input("digite o primeiro número: "))
        n2 = float(input("digite o exponencial: "))
        resultado = n1 ** n2
        print(resultado)

    os.system('cls')
    continua = input("Deseja continuar? s/n ")
    if continua.lower() == "s":
            continua == True
            print("Continuando a operação...")
    elif continua.lower() == "n":
            break
    else:
        print("Resposta inválida! Por favor, digite 's' para sair ou 'n' para continuar.")

