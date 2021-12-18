def percorrendo_arquivo():
    with open ("arquivo.txt", "r") as arquivo:
        faturamento = 0
        texto = arquivo.read()
        lista_texto = texto.split("\n") # Split serve para separar e organizar itens no texto
        lista_texto = lista_texto[1:]
        for linha in lista_texto:
            posicao_pv = linha.find(';') #somar valor depois do ponto e virgula
            valor = float(linha[posicao_pv+1 : ]) #posição do ponto e virgula +1
            faturamento += valor

        print(faturamento)
