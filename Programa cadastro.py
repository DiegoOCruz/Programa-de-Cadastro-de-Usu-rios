import utills

last_id = utills.numero_id()
if last_id == 0:
    utills.write()

''''
Programa para cadastro de usuários
'''
while True:
    print('-=' * 20)
    print()
    print('*** CADASTRO DE USUÁRIOS ***'.center(40))
    print()
    print('-=' * 20)
    print()
    print('Insira a opção desejada: \n'
          ''
          '[1] - Adicionar Usuário\n'
          '[2] - Imprimir dados\n'
          '[3] - Apagar Usuário\n'
          '[4] - Sair'
          '\n'
          '')
    opt = int(input('Digite a opcao desejada: '))
    if opt == 1:
        last_id = utills.cadastro(last_id)
    elif opt == 2:
        while True:
            opt_impressao = str(input('Deseja imprimir toda a base de dados? [S/N]: ')).upper()
            if opt_impressao == 'S':
                utills.impressao()
                break
            elif opt_impressao == 'N':
                id_usuario = int(input('Digito o Id do usuário que deseja imprimir: '))
                utills.opt_impressao_usuario(id_usuario)
                break
            else:
                print('Opção inválida.')
                opt_impressao = str(input('Deseja imprimir toda a base de dados? [S/N]: ')).upper()
    elif opt == 3:
        while True:
            print('Tem certeza que deseja apagar toda a base de Dados?\n'
                                   'As informacoes nao poderao ser recuperadas!')
            opt_apagar = str(input('Caso queira apagar digite "APAGAR": '))
            if opt_apagar == 'APAGAR':
                utills.apagar()
                break
            else:
                break
    elif opt == 4:
        print('Programa finalizado com sucesso.')
        break
    else:
        print('ERRO - Opcao nao encontrada.\n'
              'Verifique a opcao desejada e tente novamente.\n'
              '')
