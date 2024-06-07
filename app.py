import os

lista_de_restaurantes = [{'nome': 'Rei do pastel', 'categoria': 'Pastel', 'ativo': False},
                         {'nome': 'Redentor', 'categoria': 'Bar', 'ativo': True},
                         {'nome': 'Borelli', 'categoria': 'Sorvete', 'ativo': False}]

def exibir_titulo():
    '''Função que exibe o título'''
    print('''
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░
      
      ''')

def mostrar_opcoes():
    '''Função que exibe as opções no menu'''
    print('1. Cadastrar restaurante')
    print('2. Listar restaurante')
    print('3. Alterar estado de um restaurante')
    print('4. Sair\n')   

def limpar_console(titulo):
    '''Função que limpa o console e exibe o título da seção'''
    os.system('clear')
    linha = '_' * (len(titulo))
    print(titulo)
    print(linha)
    print()

def sair(): 
    '''Função usada no final de cada seção para voltar ao menu principal'''
    input('\nDigite uma tecla para voltar ao menu principal')
    main()

def finalizar_programa():
    '''Funcção que finaliza o app'''
    limpar_console('Finalizando app')

def cadastrar_restaurante():
    '''Funcão chamada na seção 1 do app, usada para cadastrar os restaurantes
    Inputs: nome e categoria do restaurante
    Output: adiciona o restaurante e sua categoria a lista de restaurantes
    '''
    limpar_console('Cadastro de novos restaurantes')
    nome_do_restaurante = input('Digite o nome do restaurante a ser cadastrado: ')
    categoria_do_restaurante = input(f'Digite a categoria do restaurante {nome_do_restaurante}: ')
    dados_do_restaurante = {'nome': nome_do_restaurante, 'categoria': categoria_do_restaurante, 'ativo': False}
    lista_de_restaurantes.append(dados_do_restaurante)
    limpar_console(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso')
    sair()

def opcao_invalida():
    '''Função chamada no menu quando o usuário não digita uma das opções válidas'''
    print('Opção inválida\n')
    sair()

def listar_restaurantes():
    '''Funcão chamada na seção 2 do app, usada para listar os restaurantes'''
    limpar_console('Listando restaurantes')
    print(f'{'Nome do restaurante'.ljust(22)} | {'Categoria'.ljust(20)} | {'Status'}')
    for restaurante in lista_de_restaurantes:
        nome_do_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativacao_do_restaurante = 'Ativo' if restaurante['ativo'] else 'Inativo'
        print(f'- {nome_do_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativacao_do_restaurante}')
    sair()

def ativar_restaurantes():
    '''Funcão chamada na seção 3 do app, usada para ativar ou desativar os restaurantes
    Input: nome do restaurante a ser ativado ou desativado
    Output: altera o estado do restaurante procurado, caso o nome bata com o de algum restaurante já presente na lista
    '''
    limpar_console('Alterando o estado de ativação de restaurantes')
    nome_procurado = input('Digite o nome do restaurante que deseja ativar ou desativar: ')
    restaurante_encontrado = False
    for restaurante in lista_de_restaurantes:
        if nome_procurado == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_procurado} foi ativado com sucesso' if restaurante['ativo'] else f'O restaurante {nome_procurado} foi desativado com sucesso'
            print(mensagem)
    if not restaurante_encontrado:
        print('Restaurante não encontrado')
    # Minha versão(funcional)
    # restaurante_encontrado = False
    # for restaurante in lista_de_restaurantes:
    #     if restaurante['nome'] == nome_procurado:
    #         if restaurante['ativo'] == restaurante_encontrado:
    #             restaurante['ativo'] = not restaurante ['ativo']
    #             print(f'O restaurante {nome_procurado} foi ativado com sucesso')
    #             break
    #         else:
    #             restaurante['ativo'] = not restaurante ['ativo']
    #             print(f'O restaurante {nome_procurado} foi desativado com sucesso')
    #             break
    # else: 
    #     print('Restaurante não encontrado')
    sair()

def escolher_opcoes():
    '''Funcão usada para navegar dentro do menu e selecionar as seções
    Input: número da seção escolhida
    Output: direcionamento para a seção escolhida ou aviso de erro caso o input não direcione a nenhuma opção
    '''
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        # opcao_escolhida = int(opcao_escolhida)
        if opcao_escolhida == 1:
            cadastrar_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            ativar_restaurantes()
        elif opcao_escolhida == 4:
            finalizar_programa()
        else:
            opcao_invalida()
    except:
        opcao_invalida()

def main():
    '''Função que abre o menu principal do app'''
    limpar_console('')
    exibir_titulo()
    mostrar_opcoes()
    escolher_opcoes()

if __name__ == '__main__':
    main()


