sexo =input('Digite seu sexo (M/F) : ')
c = 0
while sexo!= 'M' or sexo!='F':
    sexo = input('Opção não é valida.\nDigite seu sexo (M/F): ').strip().upper()
print('sexo selecionado : ', sexo)