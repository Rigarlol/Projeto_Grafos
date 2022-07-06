from grafo import Grafo

#Grafo Direcionado Representando um Torneio:
#Ex: torneio de xadrez
grafo = Grafo(5) #vertices A, B, C, D e E, que representam os jogadores do torneio

#adicionando arestas ao grafo de acordo com o observado na imagem do grafo acima
grafo.adiciona_aresta(1, 2)
grafo.adiciona_aresta(1, 4)
grafo.adiciona_aresta(2, 3)
grafo.adiciona_aresta(2, 4)
grafo.adiciona_aresta(3, 1)
grafo.adiciona_aresta(3, 5)
grafo.adiciona_aresta(4, 3)
grafo.adiciona_aresta(5, 1)
grafo.adiciona_aresta(5, 2)
grafo.adiciona_aresta(5, 4)

print('cada linha da matriz da matriz "M" corresponde a um participante, 0 representa derrota e 1 vitória')
print(grafo.matriz()) #cada linha da matriz da matriz "M" corresponde a um participante, 0 representa derrota e 1 vitória
print('-' * 30)
print('-' * 30)

#2° - Passo: fazendo o cálculo da matriz "A", onde: A = M + M²

M = grafo.matriz()
A = M + (M*M)
print('Passo: fazendo o cálculo da matriz "A", onde: A = M + M²')
print(A)
print('-' * 30)
print('-' * 30)
#3° - Passo: somando cada linha da matriz "A" e verificando a pontuação dos participantes do torneio

participantes = ['A', 'B', 'C', 'D', 'E']
for indice, linha in enumerate(A):
  print(f"Participante {participantes[indice]}: obteve {sum(linha)} pontos")