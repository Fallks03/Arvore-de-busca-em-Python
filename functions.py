import copy

def organizarGrafo(grafo):
    for chave in grafo:
        grafo[chave] = dict(sorted(grafo[chave].items(), key = lambda item: item[1]))

def buscaBfs(grafo, origem, arvore = None):
    if arvore is None:
        arvore = {}
    fila = [origem]
    indiceFila = 0
    
    while indiceFila < len(fila):
        cidadeAtual = fila[indiceFila]
        arvore.update({cidadeAtual: {}})
        
        for cidade, peso in grafo[cidadeAtual].items():
            if cidade not in fila:
                fila.append(cidade)
                arvore[cidadeAtual].update({cidade: peso})
                
        
        indiceFila += 1
    return (arvore, fila)

def buscaDfs(grafo, origem, arvore = None):
    if arvore is None:
        arvore = {}
    fila = [origem]
    visitados = set()
    visitados.add(origem)
    indiceFila = -1

    while len(arvore) < len(grafo):
        cidadeAtual = fila[indiceFila]
        indiceFila -= 1
        if cidadeAtual not in arvore:
            arvore.update({cidadeAtual: {}})
        
        for cidade, peso in grafo[cidadeAtual].items():
            if cidade not in visitados:
                visitados.add(cidade)
                arvore[cidadeAtual].update({cidade: peso})
                fila.append(cidade)
                indiceFila = -1
                break
    return (arvore, fila)

def buscaKruskal(GRAFO, origem, arvore = None):
    if arvore is None:
        arvore = {}
    grafo = copy.deepcopy(GRAFO) #faz uma cópia do grafo original para não alterar o mesmo
    menorAresta = None

    for cidade in grafo.keys():
        arvore.update({cidade: {}}) #inicializa a arvore com as cidades do grafo

    i = 0
    for cidade in grafo:
        grafo[cidade].update({'tag': {chr(65 + i)}}) #adiciona uma tag a cada cidade
        i += 1

    fila = [None] * (len(grafo) - 1) #o grafo tem n-1 arestas
    i = 0 
    while i < len(grafo) - 1: 

        menorAresta = None
        #percorre todas as cidades do grafo procurando a menor conexão
        for cidade in grafo: 
            for conexao, peso in grafo[cidade].items():
                if conexao == 'tag':
                    continue

                if menorAresta == None or peso < menorAresta[2]:
                    if ((cidade, conexao, peso) not in fila 
                        and (conexao, cidade, peso) not in fila):

                        #verifica se as cidades não tem a mesma tag
                        if grafo[cidade]['tag'].isdisjoint(grafo[conexao]['tag']): 
                            fila[i] = (cidade, conexao, peso)
                            menorAresta = (cidade, conexao, peso)
                    else:
                        continue
        
        if menorAresta == None:
            continue

        #deixa as duas cidades com tags iguais
        grafo[menorAresta[1]]['tag'].update(grafo[menorAresta[0]]['tag']) 
        grafo[menorAresta[0]]['tag'].update(grafo[menorAresta[1]]['tag'])
        
        #adiciona a nova tag a todos os vizinhos da cidade (apenas se já foram conectadas)
        for cidade in grafo:
            if not grafo[cidade]['tag'].isdisjoint(grafo[menorAresta[0]]['tag']) or not grafo[cidade]['tag'].isdisjoint(grafo[menorAresta[1]]['tag']):
                grafo[cidade]['tag'].update(grafo[menorAresta[0]]['tag'])
                grafo[cidade]['tag'].update(grafo[menorAresta[1]]['tag'])
        
        arvore[menorAresta[0]].update({menorAresta[1]: menorAresta[2]})
        arvore[menorAresta[1]].update({menorAresta[0]: menorAresta[2]})

        i += 1
    #organiza a arvore do menor ao maior
    arvore, _ = buscaBfs(arvore, origem)
    return (arvore, fila)

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

def escreverFila(fila, algoritmo):
    if algoritmo in ('KRUSKAL', '3'):
        for item in fila:
            print(f'{item[0]} --- {item[1]}\npeso: {item[2]}\n') if item != None else None
    else:
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


