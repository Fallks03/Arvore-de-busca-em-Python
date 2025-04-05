from functions import (
    organizarGrafo, escreverFila, escreverArvore,
    menorCaminho, pesoTotalArvore, 
    buscaBfs, buscaDfs, buscaKruskal
)
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
    if origem == 'Sair':
        print("Saindo...")
        break
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
        arvore, fila = buscaDfs(GRAFO, origem)

    elif tipoAlgoritmo in ('KRUSKAL', '3'):
        arvore, fila = buscaKruskal(GRAFO, origem)
    
    print("\nFila:\n")
    escreverFila(fila, tipoAlgoritmo)
    print("\nArvore:\n")
    escreverArvore(arvore)
    print(f'\nO peso total da arvore é de: {pesoTotalArvore(arvore)}Km')
    print(f'\nMenor caminho: {menorCaminho(arvore, origem, destino)}Km\n') 
                
            
        
            


