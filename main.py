def logo():
    print('==========================')
    print('       Calculadora        ')
    print('==========================')


def calculadora():
    print('Digite a operação desejada\n'
          'Adição: +\n'
          'Subtração: -\n'
          'Multiplicação: *\n'
          'Divisão: /')

    operacao = input()

    if operacao not in '+-/*':
        print(f'Operação {operacao} inválida. Tente novamente')
        calculadora()
    else:
        n1 = int(input('Digite o primeiro número: '))
        n2 = int(input('Digite o segundo número: '))

        if operacao == '+':
            print(f'{n1} + {n2} = {n1 + n2}')

        elif operacao == '-':
            print(f'{n1} - {n2} = {n1 - n2}')

        elif operacao == '*':
            print(f'{n1} * {n2} = {n1 * n2}')
        elif operacao == '/':
            if n2 == 0:
                print(f'{n1} / {n2} = ERRO')
            else:
                print(f'{n1} / {n2} = {n1 / n2}')


def resetar():
    while True:
        print('Deseja calcular novamente?(S/N)')
        opcao =input().lower()
        if opcao[0] == 's':
            calculadora()
        elif opcao[0] not in 'sn':
            print(f'Opção: {opcao} inválida. Tente novamente')
            resetar()

        elif opcao[0] == 'n':
            print('Desligando.')
            break


logo()
calculadora()
resetar()
