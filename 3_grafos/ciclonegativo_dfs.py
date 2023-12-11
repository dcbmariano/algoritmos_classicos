def bellman_ford_modificado(grafo, origem):
    """ Versão modificada do algoritmo de bellman-ford """
    global cont
    V = len(grafo)
    dist = [float('inf')] * V
    dist[origem] = 0

    for t in range(V - 1):
        for u in range(V):
            for v, peso in grafo[u]:
                # cont+=1
                if dist[u] + peso < dist[v]:
                    dist[v] = dist[u] + peso

    for u in range(V):
        for v, peso in grafo[u]:
            if dist[u] + peso < dist[v]:
                return True

    return False

# Grafo não direcionado com ciclo negativo
# grafo = [
#     [(1, -1), (2, 4)],
#     [(0, -1), (2, 3), (3, 2), (4, 2)],
#     [(0, 4), (1, 3)],
#     [(1, 2)],
#     [(1, 2)]
# ]

grafo = [
    [(1, 1)],              # Vértice 0 com uma aresta para o vértice 1 com peso 1
    [(2, 2)],              # Vértice 1 com uma aresta para o vértice 2 com peso 2
    [(0, 3), (1, 4)],      # Vértice 2 com duas arestas: vértice 0 com peso 3 e vértice 2 com peso 4
    [(0, 1)]               # Vértice 3 com uma aresta para o vértice 0 com peso 1
]


# Duplicação das arestas para considerar o grafo não direcionado
for u in range(len(grafo)):
    for v, peso in grafo[u]:
        if u != v:
            grafo[v].append((u, peso))

print(grafo)

temCiclosNegativos = False
cont = 0

for vertice in range(len(grafo)):
    if bellman_ford_modificado(grafo, vertice):
        temCiclosNegativos = True
        break

if temCiclosNegativos:
    print("O grafo contém ciclos negativos.")
else:
    print("O grafo não contém ciclos negativos.")

print(cont)

# O algoritmo de Bellman-Ford adaptado para grafos não direcionados funciona da seguinte maneira:

# Inicialize um vetor de distâncias dist com infinito para todos os vértices, exceto o vértice de origem, que tem distância zero.
# Faça V - 1 iterações, onde V é o número de vértices do grafo.
# Em cada iteração, percorra todas as arestas do grafo e relaxe as distâncias dos vértices, atualizando-as se uma rota mais curta for encontrada.
# Repita o passo anterior para garantir que todas as distâncias sejam corretamente atualizadas.
# Após as V - 1 iterações, todas as distâncias mínimas dos vértices estarão corretas se não houver ciclos negativos.
# Verifique se há ciclos negativos realizando mais uma iteração e verificando se alguma distância é atualizada. Se uma distância for atualizada, então há um ciclo negativo no grafo.
# A corretude do algoritmo pode ser explicada da seguinte forma:

# Durante as V - 1 iterações, o algoritmo relaxa as distâncias de todos os vértices, garantindo que todas as rotas mais curtas sejam encontradas.
# Se houver um ciclo negativo no grafo, durante as V - 1 iterações, o algoritmo continuará atualizando as distâncias do ciclo negativo indefinidamente.
# Portanto, ao realizar uma iteração adicional após as V - 1 iterações e verificar se alguma distância é atualizada, é possível identificar se há um ciclo negativo no grafo.
# Se alguma distância for atualizada nessa iteração adicional, então há um ciclo negativo no grafo, caso contrário, não há ciclos negativos.
# Dessa forma, o algoritmo de Bellman-Ford adaptado para grafos não direcionados é capaz de detectar ciclos negativos corretamente.


# A análise assintótica do algoritmo de Bellman-Ford pode ser dividida em duas partes:

# Construção do grafo: A construção do grafo não está incluída no algoritmo de Bellman-Ford em si, mas é relevante considerar sua complexidade. Se o grafo for representado por uma lista de adjacência, a construção do grafo terá uma complexidade de tempo de O(E), onde E é o número de arestas do grafo.

# Algoritmo de Bellman-Ford: A complexidade de tempo do algoritmo de Bellman-Ford é O(V * E), onde V é o número de vértices e E é o número de arestas do grafo. Durante as V - 1 iterações do algoritmo, todas as arestas são percorridas e as distâncias são relaxadas, resultando em um total de V * E operações. Além disso, uma iteração adicional é realizada para verificar se há ciclos negativos, o que adiciona um custo adicional de E operações.

# Portanto, a complexidade de tempo total do algoritmo de Bellman-Ford para detectar ciclos negativos em grafos não direcionados é O(E + V * E) = O(V * E).

# É importante notar que a complexidade de espaço do algoritmo é O(V), pois é necessário armazenar as distâncias mínimas para cada vértice.

# Em resumo, a análise assintótica do algoritmo de Bellman-Ford para detectar ciclos negativos em grafos não direcionados é O(V * E), onde V é o número de vértices e E é o número de arestas do grafo.