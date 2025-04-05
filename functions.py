def organizarGrafo(grafo):
    for chave in grafo:
        grafo[chave] = dict(sorted(grafo[chave].items(), key = lambda item: item[1]))

def escreverArvore(arvore, nivel=1, cidade=None):
    if cidade is None:
        cidade = next(iter(arvore)) #pega a primeira chave da arvore
        print(cidade + " (raiz)")

    if cidade in arvore:
        for chave, valor in arvore[cidade].items():
            print(" " * (nivel * 4) + f"↳ {chave} ({valor})")
            escreverArvore(
                cidade=chave,
                nivel=(nivel + 1),
                arvore=arvore
            )

def escreverFila(fila):
    print("Q: {", end="")
    for i in fila:
        print(i, end=", ") if i != fila[-1] else print(i, end="")
    print("}")

def menorCaminho(arvore, origem, destino):
    #a busca do menor caminho se basea em pegar o destino e fazer um caminho reverso até a origem
    #o algoritmo busca na arvore qual cidade tem uma conexão igual a da cidade atual da iteração
    #se ele achar, a cidade pai se torna a atual, repita isso até achar origem
    #depois a função retorna a lista do caminho de trás pra frente.
    cidadeAtual = destino
    menorCaminho = [destino]
    txtCaminho = ''
    pesoCaminho = 0

    while cidadeAtual != origem:
        
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
        
def pesoTotalArvore(arvore):
    pesoTotal = 0
    for cidade in arvore:
        for peso in arvore[cidade].values():
            pesoTotal += peso
    return pesoTotal


