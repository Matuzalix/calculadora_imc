
nome = input('Digite o nome do paciente: ')
altura = float(input('Digite a altura do paciente: '))
peso = float(input('Digite o peso do paciente: '))

nome_str = str(nome)
altura_float = float(altura)
peso_float = float(peso)

imc = peso_float / (altura_float ** 2)

if imc < 18.5:
    resultado = 'Abaixo do Peso Normal'
elif imc > 18.5 and imc < 25:
    resultado = 'Peso Normal'
elif imc > 25 and imc < 30:
    resultado = 'Acima do Peso'
elif imc > 30 and imc < 35:
    resultado = 'Obesidade Classe I'
elif imc > 35 and imc < 40:
    resultado = 'Obesidade Classe II'
else:
    imc >= 40
    resultado = 'Obesidade Classe III'


print(f'Nome: {nome_str} tem {altura_float} de altura')
print(f'Pesa: {peso_float}kg, e seu IMC é:')
print(f'{imc:.2f}')
print(f'Avaliação Final: {resultado}')
