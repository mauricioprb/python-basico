from Cidade import Cidade

class Grafo:
    def __init__(self):
        self.cidades = []
        self.matriz_adjacencia = []

    def adicionar_cidade(self, cidade):
        self.cidades.append(cidade)
        num_cidades = len(self.cidades)
        for linha in self.matriz_adjacencia:
            linha.append(0)
        self.matriz_adjacencia.append([0] * num_cidades)

    def adicionar_distancia(self, cidade1, cidade2, distancia):
        indice_cidade1 = self.cidades.index(cidade1)
        indice_cidade2 = self.cidades.index(cidade2)
        self.matriz_adjacencia[indice_cidade1][indice_cidade2] = distancia
        self.matriz_adjacencia[indice_cidade2][indice_cidade1] = distancia

    def imprimir_matriz_adjacencia(self):
        for linha in self.matriz_adjacencia:
            print(' '.join(map(str, linha)))
