import csv

def cadastro(last_id):
    cpfs_invalidos = ['11111111111',
                      '22222222222',
                      '33333333333',
                      '44444444444',
                      '55555555555',
                      '66666666666',
                      '77777777777',
                      '88888888888',
                      '99999999999',
                      '00000000000']
    id = last_id + 1
    print('Insira os dados:')
    nome = str(input('Nome: '))
    while nome.isnumeric() == True:
        print('Nome inválido.')
        nome = str(input('Nome: '))
    idade = str(input('Idade: '))
    while idade.isnumeric() == False:
        print('Idade Inválida. Insira apenas números!')
        idade = str(input('Idade: '))
    email = str(input('E-mail: '))
    cpf = str(input('CPF: '))
    cpf_validacao = cpf.replace('.','').replace('-','')
    #print(len(cpf_validacao))
    #...
    while (len(cpf_validacao) != 11) or (cpf_validacao in cpfs_invalidos) \
            or (not valida_cpf_dv1(cpf_validacao)) or (not valida_cpf_dv2(cpf_validacao)): #.
        #print(len(cpf_validacao))
        if len(cpf_validacao) != 11:
            print('CPF inválido. O CPF deve conter 11 digitos.')
        if cpf_validacao in cpfs_invalidos:
            print('CPF Inválido.')
        cpf = str(input('CPF: '))
        cpf_validacao = cpf.replace('.', '').replace('-', '')

    valida_cpf_dv1(cpf_validacao)

    #if last_id == 1:
    #    write(id,nome,idade,email,cpf)
    #else:
    if valida_cpf_dv1(cpf_validacao) and valida_cpf_dv2(cpf_validacao):
        append(id,nome,idade,email,cpf)
        return id
    else:
        print('Cadastro não realizado. O CPF é inválido.')
        return last_id

def impressao():
    with open('usuarios.csv','r') as arquivo:
        leitor= csv.reader(arquivo)
        for row in leitor:
            print(row)
            print('')

def opt_impressao_usuario(id_usuario):
    with open('usuarios.csv', 'r') as arquivo:
        leitor = csv.reader(arquivo)
        for index, row in enumerate(leitor):
            if index == id_usuario:
                print('')
                print(["id", "nome", "idade", "email", "cpf"])
                print(row)
                print('')
                break
def apagar():
    with open('usuarios.csv','w',newline='') as arquivo:
        escritor = csv.writer(arquivo)
        escritor.writerow(["id", "nome", "idade", "email", "cpf"])
        print('Dados apagados com sucesso!')

def alterar_usuario():
    pass

def valida_cpf_dv1(cpf_validacao):
    cpf_array = []
    for i in cpf_validacao:
        cpf_array.append(i)
    #print(cpf_array)
    dv_1 = int(cpf_array[9])
    #print(type(dv_1))
    valida_dv1 = cpf_array[0:9]
    #print(valida_dv1)
    controlador = 10
    soma = 0
    for i in valida_dv1:
        multiplicacao = int(i) * controlador
        #print(f'{i} x {controlador} = {multiplicacao}')
        controlador = controlador - 1
        soma += multiplicacao
    #print(soma)
    resto = (soma * 10) % 11
    #print(resto)
    if resto == 10 or resto == 11:
        resto = 0
    #print(f'{resto} - {type(resto)}')
    if dv_1 != resto:
        print('Digito verificador inválido!')
        return False
    else:
        #print('dv1 ok')
        return valida_cpf_dv2(cpf_validacao)

def valida_cpf_dv2(cpf_validacao):
    cpf_array = []
    for i in cpf_validacao:
        cpf_array.append(i)
    #print(cpf_array)
    dv_2 = int(cpf_array[10])
    #print(type(dv_1))
    valida_dv2 = cpf_array[0:10]
    #print(valida_dv1)
    controlador = 11
    soma = 0
    for i in valida_dv2:
        multiplicacao = int(i) * controlador
        #print(f'{i} x {controlador} = {multiplicacao}')
        controlador = controlador - 1
        soma += multiplicacao
    #print(soma)
    resto = (soma * 10) % 11
    #print(resto)
    if resto == 10 or resto == 11:
        resto = 0
    #print(f'{resto} - {type(resto)}')
    if dv_2 != resto:
        print('Digito verificador inválido!')
        return False
    else:
        #print('dv2 ok')
        return True

def numero_id():
    last_id = 0
    try:
        with open('usuarios.csv','r') as arquivo:
            leitor = csv.reader(arquivo)
            next(leitor)
            ids = [int(row[0]) for row in leitor]
            if ids:
                last_id = max(ids)
    except FileNotFoundError:
        pass
    return last_id

def write():
    with open('usuarios.csv','w',newline='') as arquivo:
        escritor = csv.writer(arquivo)
        escritor.writerow(["id", "nome", "idade", "email", "cpf"])
        #escritor.writerow([id, nome, idade, email, cpf])
        #return print('\n'
        #             'Usuário cadastrado com sucesso\n'
        #             '')

def append(id,nome,idade,email,cpf):
    with open('usuarios.csv','a',newline='') as arquivo:
        escritor = csv.writer(arquivo)
        escritor.writerow([id, nome, idade, email, cpf])
        return print('\n'
                     'Usuário cadastrado com sucesso\n'
                     '')



