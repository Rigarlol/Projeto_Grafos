# Projeto_Grafos
Projeto final da disciplina Teoria dos Grafos


TÍTULO DO PROJETO: Ranking the Participants in a Tournament
  EQUIPE: João Paulo de Melo Bispo;
  Luis Henrique da Silva;
  Matheus Ferreira da Silva.
  

Contextualização

Tendo em vista a existência de inúmeros tipos de torneios e competições, sabemos
que uma métrica de avaliação desses participantes é a classificação destes, essa por sua
vez é se dá em decorrência de diversas disputas ao decorrer do evento. Porém, nem
sempre esses critérios de classificação são justos e ideais, fazendo então com que um
determinado participante, que pode ser uma equipe ou um indivíduo, venha a ser
prejudicado. Dessa forma, fazer a implementação de um algoritmo que vise realizar essa
classificação, seguindo critérios mais justos, se faz necessário para auxiliar a organização
do torneio em questão

Problema

Dada uma competição de um torneio qualquer, onde todos os participantes se enfrentam, se
faz necessária a classificação desses participantes, mas qual a melhor maneira de fazê-la?
É importante notar que os critérios de classificação de um torneio nem sempre são justos,
pois pode vir a trazer os mesmo privilégios e prejuízos para o participante vencedor e o
derrotado.

Objetivo(s)

O objetivo é o de, com o auxílio da utilização da representação computacional de
grafos 1. Usar grafos para modelar o problema. 2. Implementar um algoritmo capaz de fazer
uma classificação justa dos participantes de um torneio.

Método

O algoritmo utilizado para a resolução do problema baseia-se na técnica
denominada “Grafos dirigidos por dominância” (GDD), onde os participantes mais bem
colocados são os que derrotaram outros participantes ou os que derrotaram um participante
que venceu uma partida contra ele. Esse algoritmo possui os seguintes passos:

  ● Modelar o grafo em forma de uma matriz M;
  ● Cada linha A da matriz M representa um participante do torneio;
  ● Calcular, a partir de M, uma matriz A, tal que A = M + M²;
  ● Calcula as somas de cada linha de A, ao fim, as linhas as com maiores somas,
identificam os participantes mais bem colocados.
