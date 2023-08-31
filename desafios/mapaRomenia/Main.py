from Grafo import Grafo

def main():
    grafo = Grafo()

    arquivo = 'mapaRomenia.txt'
    with open(arquivo, 'r') as f:
        for linha in f:
            cidade1, cidade2, distancia = linha.strip().split('@')
            if cidade1 not in grafo.cidades:
                grafo.adicionar_cidade(cidade1)
            if cidade2 not in grafo.cidades:
                grafo.adicionar_cidade(cidade2)
            grafo.adicionar_distancia(cidade1, cidade2, int(distancia))

    grafo.imprimir_matriz_adjacencia()


if __name__ == "__main__":
    main()
