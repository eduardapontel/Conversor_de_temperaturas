bordas = '\033[037m-=-\033[m' * 12
print(bordas)
print('{:^35}'.format('CONVERSOR DE TEMPERATURAS'))
print(bordas)
print()

c = ''

while type(c) != float:
    try:
        c = float(input('Informe a temperatura em °C: '))
    except:
        print('Por favor digite uma temperatura válida!')

print(bordas)
print('F -> Para converter para Fahrenheit')
print('K -> Para converter para Kelvin')
print(bordas)

while True:
    convert = input('Digite a opção desejada: ').strip().upper()
    match convert:
        case 'F':
            print(f'\nA temperatura corresponde a {c/5*9+32:.2f}°F')
            break
        case 'K':
            print(f'\nA temperatura corresponde a {c+273.15:.2f}K')
            break
        case _:
            print('Por favor digite uma opção válida!')
