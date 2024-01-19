import os

restaurantes = []

def exibir_nome_do_programa():
    print('𝑺𝑨𝑩𝑶𝑹 𝑬𝑿𝑷𝑹𝑬𝑺𝑺\n')

def exibir_opcoes():
    '''Imprime as opções do app'''
    print('1. Cadastrar restaurante')
    print('2. Listar restaurante')
    print('3. Alternar estado do restaurante')
    print('4. Sair\n')

def finalizar_app():
    '''Função para finalizar e sair do app'''
    os.system('cls')
    print('Aplicativo finalizado\n')

def voltar_ao_menu_principal():
    '''Função para retornar ao Menu Principal'''
    input('\nDigite uma tecla para voltar ao menu principal. ')
    main()

def exibir_subtitulo(texto):
    '''Função para iniciar qualquer das opções selecionadas'''
    os.system('cls')
    linha = '*' * (len(texto) + 6)
    print(linha)
    print(f'** {texto} **')
    print(linha)
    print()

def opcao_invalida():
    '''Função de retorno para o Menu Principal quando temos uma opção selecionada de forma invalida'''
    exibir_subtitulo('Opção inválida!')
    voltar_ao_menu_principal()
    
def cadastrar_novo_restaurante():
    '''Função para cadastrar um novo restaurante - durante o cadastro ele permanecerá inativo'''
    exibir_subtitulo('Cadastro de novos restaurantes')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ').upper()
    categoria = input(f'Digite a categoria do restaurante {nome_do_restaurante}: ').upper()
    dados_do_restaurante = {'nome':nome_do_restaurante, 'categoria':categoria, 'ativo':False}
    restaurantes.append(dados_do_restaurante)
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!\n')
    voltar_ao_menu_principal()

def listar_restaurantes():
    '''Função para listar os restaurantes cadastrados com sua categoria e status'''
    exibir_subtitulo('Lista dos restaurantes')
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = 'ATIVADO' if restaurante['ativo'] else 'DESATIVADO'
        print(f'=> {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}')
    voltar_ao_menu_principal()

def alternar_estado_restaurante():
    '''Função para ativar ou desativar o restaurante'''
    exibir_subtitulo('Alternar estado do restaurante')
    nome_restaurante = input('Digite o nome do restaurante que deseja alternar o estado: ').upper()
    restaurante_encontrado = False
    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso!' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso!'
            print(mensagem)
    if not restaurante_encontrado:
        print(f'O restaurante {nome_restaurante} não foi encontrado!')
    voltar_ao_menu_principal()

def escolher_opcao():
    '''Função para direcionar após escolha da opção'''
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            alternar_estado_restaurante()
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()

def main():
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()