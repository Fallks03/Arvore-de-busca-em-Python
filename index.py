import functions

grafo = {
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
functions.organizarGrafo(grafo)

#imprime as cidades do grafo
for chave in grafo:
    print(chave)

while True:
    arvore = {}

    origem = input("\nQual a cidade de origem?\n> ")
    if not(origem in grafo):
        print("Esta cidade não existe no grafo!")
        continue

    while True:
        destino = input("\nQual a cidede de destino?\n> ")
        if not(destino in grafo):
            print("Esta cidade não existe no grafo!")
            continue
        break

    while True:
        tipoAlgoritmo = input("\nQual o tipo de algoritmo de busca? (BFS/DSF)\n> ").upper()
        if tipoAlgoritmo not in ('BFS', 'DSF'):
            print("Algortimo inválido!")
            continue
        break

    if tipoAlgoritmo == 'BFS':
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
        functions.escreverFila(fila)
        print("\nArvore:\n")
        functions.escreverArvore(arvore)

    elif tipoAlgoritmo == 'DSF':
        pilha = [origem]
        visitados = set()

        while true:
            cidadeAtual = pilha[-1]
            arvore.update({cidadeAtual: {}})
            
            for cidade, peso in grafo[cidadeAtual]:
                if cidade not in visitados:
                    visitados.append(cidade)
                    arvore[cidadeAtual].update({cidade: peso})
                    pilha.append(cidade)
        
                
            
        
            


