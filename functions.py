def organizarGrafo(grafo):
    for chave in grafo:
        grafo[chave] = dict(sorted(grafo[chave].items(), key = lambda item: item[1]))

def escreverArvore(arvore):
    for chave in arvore:
        print(chave + ":", arvore[chave])

def escreverFila(fila):
    print("Q: {", end="")
    for i in fila:
        print(i, end=", ") if i != fila[-1] else print(i, end="")
    print("}")

def menorCaminho(arvore, destino):
    cidadeAtual = destino
    cidadeOrigem = next(iter(arvore.keys())) #pega o primeiro item da arvore
    menorCaminho = [destino]
    txtCaminho = ''
    pesoCaminho = 0
    while cidadeAtual != cidadeOrigem:
        
        for cidade, conexoes in arvore.items():
            if cidadeAtual in conexoes:
                menorCaminho.append(cidade)
                for c, peso in arvore[cidade].items():
                    if c == cidadeAtual:
                        pesoCaminho += peso
                        
                cidadeAtual = cidade
                break
            
    for i in range(1, len(menorCaminho)+1):
        txtCaminho += f' -> {menorCaminho[-i]}' if i != 1 else f'{menorCaminho[-i]}'
        if menorCaminho[-i] == destino:
            return f'{txtCaminho} {pesoCaminho}'
