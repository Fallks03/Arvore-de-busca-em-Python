import functions

grafo = {
    "Campinas": {"Paulínia": 23, "Monte Mor": 22, "Indaiatuba": 20},
    "Paulínia": {"Americana": 22, "Campinas": 23},
    "Americana": {"Paulínia": 22, "Sumaré": 18},
    "Sumaré": {"Americana": 18, "Monte Mor": 15},
    "Monte Mor": {"Campinas": 22, "Sumaré": 15, "Capivari": 25, "Indaiatuba": 20},
    "Capivari": {"Monte Mor": 25, "Tietê": 30, "Piracicaba": 32},
    "Piracicaba": {"Capivari": 32, "Americana": 30},
    "Indaiatuba": {"Monte Mor": 20, "Salto": 20},
    "Salto": {"Indaiatuba": 20, "Itu": 10, "Porto Feliz": 12},
    "Itu": {"Salto": 10, "Sorocaba": 8},
    "Sorocaba": {"Itu": 8, "Boituva": 23},
    "Boituva": {"Sorocaba": 23, "Porto Feliz": 12, "Tatuí": 12},
    "Porto Feliz": {"Boituva": 12, "Salto": 12, "Tietê": 30},
    "Tietê": {"Capivari": 30, "Porto Feliz": 30, "Tatuí": 25},
    "Tatuí": {"Boituva": 12, "Tietê": 25, "Sorocaba": 17}
}

arvore = {}

quantCidades = len(grafo)

origem = input("Qual a cidade de origem?\n> ")
if not(origem in grafo):
    print("!")
    
destino = input("qual a cidede de destino?\n> ")
if not(destino in grafo):
    print("!")

tipoAlgoritmo = input("Qual o tipo de algoritmo de busca?\n> ").upper()
if tipoAlgoritmo not in ('BFS', 'DSF'):
    print("!")

if tipoAlgoritmo == 'BFS':
    fila = [origem]
    menorCaminho = [origem]
    pesoCaminho = 0
    cidadeAtual = origem
    indiceFila = 0
    
    while len(fila) < quantCidades:
        arvore.update({cidadeAtual: {}})
        print(arvore)
        for cidade, peso in grafo[cidadeAtual].items():
            if cidade not in fila:
                fila.append(cidade)
                arvore[cidadeAtual].update({cidade: peso})
                
        
        indiceFila += 1
        cidadeAtual = fila[indiceFila]


    


