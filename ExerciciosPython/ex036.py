valor = float(input('digite o valor da casa : '))
salario = float(input('digite o valor do seu salario : '))
anos = int(input('em quantos anos você vai pagar : '))
parcela = valor/(anos*12)
if parcela > salario*0.30:
    print('empréstimo negado')
else:
    print('emprestimo aprovado')
