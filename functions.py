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