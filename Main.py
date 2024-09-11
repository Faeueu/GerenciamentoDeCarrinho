from carrinho.Carrinho import inserir_item, carrinho
from funcoes.Acrescimo import aplicar_acrescimo_item, distribuir_acrescimo_total
from funcoes.Desconto import aplicar_desconto_item, distribuir_desconto_total
from vendas.FinalizarVenda import finalizar_venda

def mostrar_menu():
    print('\nMenu:')
    print('1. Inserir item ao carrinho')
    print('2. Acréscimo de item')
    print('3. Desconto de item')
    print('4. Acréscimo total')
    print('5. Desconto total')
    print('6. Finalizar venda')

while True:
    mostrar_menu()
    opcao = input('Escolha uma opção: ')

    if opcao == '1':
        codigo = input('Digite o código do item: ')
        nome = input('Digite o nome do item: ')
        descricao = input('Digite a descrição do item: ')
        valor = float(input('Digite o valor do item: '))
        inserir_item(codigo, nome, descricao, valor)

    elif opcao == '2':
        codigo = input('Digite o código do item: ')
        acrescimo = float(input('Digite o valor do acréscimo: '))
        aplicar_acrescimo_item(codigo, acrescimo)

    elif opcao == '3':
        codigo = input('Digite o código do item: ')
        desconto = float(input('Digite o valor do desconto: '))
        aplicar_desconto_item(codigo, desconto)

    elif opcao == '4':
        acrescimo_total = float(input('Digite o valor total de acréscimo: '))
        distribuir_acrescimo_total(carrinho, acrescimo_total)

    elif opcao == '5':
        desconto_total = float(input('Digite o valor total de desconto: '))
        distribuir_desconto_total(carrinho, desconto_total)

    elif opcao == '6':
        finalizar_venda(carrinho)
        break

    else:
        print('Opção inválida. Tente novamente.')
