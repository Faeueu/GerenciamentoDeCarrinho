from carrinho.Carrinho import encontrar_item, mostrar_estado_atual

def aplicar_desconto_item(codigo, desconto):
    item = encontrar_item(codigo)
    if item:
        item['desconto'] += desconto
        item['total'] -= desconto
        print(f'Desconto de R${desconto:.2f} aplicado com sucesso ao item "{item["nome"]}"!')
        mostrar_estado_atual()


def distribuir_desconto_total(carrinho, desconto_total):
    if carrinho:
        desconto_por_item = desconto_total / len(carrinho)
        for item in carrinho:
            item['desconto'] += desconto_por_item
            item['total'] -= desconto_por_item
        print(f'Desconto total de R${desconto_total:.2f} distribuído igualmente entre os itens.')
        mostrar_estado_atual()

