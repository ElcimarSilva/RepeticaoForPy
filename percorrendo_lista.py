
def percorre_lista_produtos():
    lista_produtos = ['faca', 'garfo', 'panela', 'frigideira', 'blabla']

    for produto in lista_produtos:
        print(produto.capitalize())


def percorre_lista_precos():
    lista_precos = [10,9,8,7]
    for preco in lista_precos:
        imposto = preco * 0.1
        print(imposto)

