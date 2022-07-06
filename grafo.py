#Grafo Direcionado Representando um Torneio:
#Ex: torneio de xadrez
import numpy as np

class Grafo:

    def __init__(self, vertices):
        self.vertices = vertices
        self.grafo = [[0]*self.vertices for i in range(self.vertices)]

    def adiciona_aresta(self, u, v):
        self.grafo[u-1][v-1] = 1

    def matriz(self):
        matriz = list()
        for i in range(self.vertices):
            matriz.append(self.grafo[i])
        return np.array(matriz)

