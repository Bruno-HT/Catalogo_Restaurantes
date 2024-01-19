import os

restaurantes = []

def exibir_nome_do_programa():
    print('𝑺𝑨𝑩𝑶𝑹 𝑬𝑿𝑷𝑹𝑬𝑺𝑺\n')

def exibir_opcoes():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurante')
    print('3. Ativar restaurante')
    print('4. Sair\n')

def finalizar_app():
    os.system('cls')
    print('Aplicativo finalizado\n')

def voltar_ao_menu_principal():
    input('\nDigite uma tecla para voltar ao menu principal. ')
    main()

def exibir_subtitulo(texto):
    os.system('cls')
    print(texto)
    print()

def opcao_invalida():
    exibir_subtitulo('Opção inválida!')
    voltar_ao_menu_principal()
    
def cadastrar_novo_restaurante():
    exibir_subtitulo('Cadastro de novos restaurantes')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar:').upper()
    restaurantes.append(nome_do_restaurante)
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!\n')
    voltar_ao_menu_principal()

def listar_restaurantes():
    exibir_subtitulo('Lista dos restaurantes')
    for restaurante in restaurantes:
        print(f'=> {restaurante}')
    voltar_ao_menu_principal()

def escolher_opcao():
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            print('Ativar restaurante')
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