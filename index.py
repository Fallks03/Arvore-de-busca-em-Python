from functions import organizarGrafo, escreverFila, escreverArvore, menorCaminho, pesoTotalArvore, buscaBfs
import copy

GRAFO = {
    "Campinas": {"Paulínia": 25, "Sumaré": 23, "Monte Mor": 22, "Indaiatuba": 20},
    "Paulínia": {"Americana": 22, "Campinas": 25},
    "Americana": {"Paulínia": 22, "Sumaré": 18, "Piracicaba": 30},
    "Sumaré": {"Americana": 18, "Campinas": 23},
    "Monte Mor": {"Campinas": 22, "Capivari": 15},
    "Capivari": {"Monte Mor": 15, "Tietê": 30, "Piracicaba": 32, "Salto": 25},
    "Piracicaba": {"Capivari": 32, "Americana": 30, "Tietê": 35},
    "Indaiatuba": {"Campinas": 20, "Salto": 20},
    "Salto": {"Indaiatuba": 20, "Itu": 10, "Capivari": 25},
    "Itu": {"Salto": 10, "Sorocaba": 8, "Porto Feliz": 12},
    "Sorocaba": {"Itu": 8, "Boituva": 23},
    "Boituva": {"Sorocaba": 23, "Porto Feliz": 12, "Tatuí": 17},
    "Porto Feliz": {"Boituva": 12, "Tietê": 30, "Itu": 12},
    "Tietê": {"Capivari": 30, "Porto Feliz": 30, "Tatuí": 25, "Piracicaba": 35},
    "Tatuí": {"Boituva": 17, "Tietê": 25}
}

#organiza os valores de cada chave do grafo do menor ao maior dentro do dicionario
organizarGrafo(GRAFO)

fila = None #declaração da fila

#imprime as cidades do grafo
for chave in GRAFO:
    print(chave)

while True:
    arvore = {}
    fila = None #declaração da fila

    origem = input("\nQual a cidade de origem?\n> ").capitalize() #capitalize transforma a primeira letra em maiúscula e o resto em minúscula
    if not(origem in GRAFO):
        print("Esta cidade não existe no grafo!")
        continue

    while True:
        destino = input("\nQual a cidade de destino?\n> ").capitalize()
        if origem == destino:
            print("A origem e o destino não podem ser iguais!")
            continue
        if not(destino in GRAFO):
            print("Esta cidade não existe no grafo!")
            continue
        break

    while True:
        tipoAlgoritmo = input("\nQual o tipo de algoritmo de busca?\n1 - BFS\n2 - DFS\n3 - Kruskal\n> ").upper()
        if tipoAlgoritmo not in ('BFS', 'DFS', 'KRUSKAL', '1', '2', '3'):
            print("Algortimo inválido!")
            continue
        break

    if tipoAlgoritmo in ('BFS', '1'):
        arvore, fila = buscaBfs(GRAFO, origem) 
        
    elif tipoAlgoritmo in ('DFS', '2'):
        fila = [origem]
        visitados = set()
        visitados.add(origem)
        indiceFila = -1

        while len(arvore) < len(GRAFO):
            cidadeAtual = fila[indiceFila]
            indiceFila -= 1
            if cidadeAtual not in arvore:
                arvore.update({cidadeAtual: {}})
            
            for cidade, peso in GRAFO[cidadeAtual].items():
                if cidade not in visitados:
                    visitados.add(cidade)
                    arvore[cidadeAtual].update({cidade: peso})
                    fila.append(cidade)
                    indiceFila = -1
                    break

    elif tipoAlgoritmo in ('KRUSKAL', '3'):
        grafo = copy.deepcopy(GRAFO) #faz uma cópia do grafo original para não alterar o mesmo
        menorAresta = None

        for cidade in grafo.keys():
            arvore.update({cidade: {}}) #inicializa a arvore com as cidades do grafo

        i = 0
        for cidade in grafo:
            grafo[cidade].update({'tag': {chr(65 + i)}}) #adiciona uma tag a cada cidade
            i += 1

        fila = [None] * (len(grafo) * 2) 
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
        arvore, _ = buscaBfs(arvore, origem)
        #organiza a arvore do menor ao maior
    
    print("\nFila:\n")
    escreverFila(fila, tipoAlgoritmo)
    print("\nArvore:\n")
    escreverArvore(arvore)
    print(f'\nO peso total da arvore é de: {pesoTotalArvore(arvore)}Km')
    print(f'\nMenor caminho: {menorCaminho(arvore, origem, destino)}Km\n') 
                
            
        
            


