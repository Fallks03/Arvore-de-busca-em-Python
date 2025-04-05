from functions import organizarGrafo, escreverFila, escreverArvore, menorCaminho, pesoTotalArvore
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
        fila = [origem]
        indiceFila = 0
        
        while indiceFila < len(fila):
            cidadeAtual = fila[indiceFila]
            arvore.update({cidadeAtual: {}})
            
            for cidade, peso in GRAFO[cidadeAtual].items():
                if cidade not in fila:
                    fila.append(cidade)
                    arvore[cidadeAtual].update({cidade: peso})
                    
            
            indiceFila += 1
        
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
        grafo = copy.deepcopy(GRAFO) #faz uma cópia do grafo original para não alterar o original
        menorAresta = None
        pesoTotal = 0

        i = 0
        for cidade in grafo:
            grafo[cidade].update({'tag': {chr(65 + i)}}) #adiciona uma tag ("cor") a cada cidade
            i += 1

        #cria uma lista de visitados com o tamanho do grafo
        visitados = [None] * (len(grafo)) 
        #enquanto a lista de visitados não estiver cheia
        i = 0 
        while i < len(grafo): 

            menorAresta = None
            #percorre todas as cidades do grafo procurando a menor conexão
            for cidade in grafo: 
                for conexao, peso in grafo[cidade].items():
                    if conexao == 'tag':
                        continue

                    if menorAresta == None or peso < menorAresta[2]:
                        if ((cidade, conexao, peso) not in visitados 
                            and (conexao, cidade, peso) not in visitados):

                            #verifica se as cidades não tem a mesma tag (cor)
                            if grafo[cidade]['tag'] != grafo[conexao]['tag']: 
                                visitados[i] = (cidade, conexao, peso)
                                menorAresta = (cidade, conexao, peso)
                        else:
                            continue
            
            #deixa as duas cidades com a mesma tag (cor)
            grafo[menorAresta[1]]['tag'] = grafo[menorAresta[0]]['tag'] 
            if menorAresta[0] in arvore:
                arvore[menorAresta[0]].update({menorAresta[1]: menorAresta[2]})
            else:
                arvore.update({menorAresta[0]: {menorAresta[1]: menorAresta[2]}})
            i += 1
                
    escreverFila(fila) if fila else None
    print("\nArvore:\n")
    escreverArvore(arvore, origem)
    print(f'\nO peso total da arvore é de: {pesoTotalArvore(arvore)}Km')
    print(f'\nMenor caminho: {menorCaminho(arvore, origem, destino)}Km\n') 
                
            
        
            


