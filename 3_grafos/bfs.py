# BFS algorithm in Python
import collections
import random

def busca_em_largura(G, vertice_origem=0, mostrar_caminho=True, alvo=-1, mostrar_alvo=True):
    ''' busca em largura '''
    visitado, fila = set(), collections.deque([vertice_origem])
    visitado.add(vertice_origem)
    caminho = []

    if mostrar_alvo and alvo != -1:
        print("Alvo:", alvo)

    while fila:
        # Retira um vertice da fila
        vertice = fila.popleft()
        caminho.append(vertice)

        if mostrar_caminho:    
            if vertice == alvo:
                print(caminho)
                return caminho

        # Se não visitado, marca como visitado e enfilera
        for vizinho in G[vertice]:
            if vizinho not in visitado:
                visitado.add(vizinho)
                fila.append(vizinho)

    if mostrar_caminho:
        print(caminho)
    else: 
        return caminho


def busca_em_profundidade(G, inicio=0, visitado=None, mostrar_caminho=True, alvo=-1, mostrar_alvo=True):
    ''' busca em profundidade '''
    if mostrar_caminho: 
        if mostrar_alvo and alvo != -1:
            print("Alvo:", alvo)

        if visitado != None:
            if inicio not in visitado:  # imprime o valor visitado
                print(inicio, end=" ")


    if visitado is None:
        visitado = set()
    visitado.add(inicio)

    try:
        for next in G[inicio] - visitado:
            if inicio == alvo:
                return
            busca_em_profundidade(G, next, visitado, alvo=alvo, mostrar_alvo=False)
    except:
        return

    return visitado

lista_de_adjacencias = {} # lista de adjacencia
vertices = []

def ad_vertice(vertice):
    lista_de_adjacencias[vertice] = []

 
def ad_aresta(node1, node2, bidirecional = True):
    temp = []  
    temp.extend(lista_de_adjacencias[node1])
    temp.append(node2) 
    lista_de_adjacencias[node1] = set(temp)

    if bidirecional:
        temp = []  
        temp.extend(lista_de_adjacencias[node2])
        temp.append(node1)
        lista_de_adjacencias[node2] = set(temp)
       

def grafo():
    ''' imprime o grafo '''
    print("*** GRAFO ***")
    print("Vértice -> [Lista de adjacências]")
    for vertice in lista_de_adjacencias:
        print(vertice, " -> ", [i for i in lista_de_adjacencias[vertice]])
 


n = 96295 # 1000 vertices

#adiciona vertices
for i in range(n): 
    ad_vertice(i)

#adiciona arestas
for i in range(n//5): # 50 mil arestas
    a = random.randint(0, n-1)
    b = random.randint(0, n-1)

    ad_aresta(a, b, False)

# imprime o grafo 
#grafo()

print("\nBusca em largura:")
busca_em_largura(lista_de_adjacencias)
print("Busca em profundidade:")
busca_em_profundidade(lista_de_adjacencias)

print("\n\nBusca em largura com alvo:")
busca_em_largura(lista_de_adjacencias, 0, alvo=2)
print("Busca em profundidade com alvo:")
busca_em_profundidade(lista_de_adjacencias, 0, alvo=8)

print("\n---")


vazio = 0
subgrafos = []
for i in range(n):
    if len(lista_de_adjacencias[i]) > 0:
        #print("\n\nBusca em profundidade para:", i)
        #busca_em_profundidade(lista_de_adjacencias, i)

        #print("\n\nBusca em largura para:", i)
        subgrafos.append(busca_em_largura(lista_de_adjacencias, i, mostrar_caminho = False))
    else:
        vazio += 1

print("\nVértices vazios:", vazio)

custo_biblioteca = 10
custo_estrada = 9

# custo_singlegrafos = (custo_biblioteca * vazio) 
custo_singlegrafos = custo_biblioteca * vazio
# custo_subgrafos = (n_subgrafos * custo_biblioteca + custo_estrada * elementos_em_subgrafos)

n_subgrafos = len(subgrafos)
elementos_em_subgrafos = 0

for subgrafo in subgrafos:
    elementos_em_subgrafos += len(subgrafo)

custo_subgrafos = (n_subgrafos * custo_biblioteca) + (custo_estrada * elementos_em_subgrafos)
# custo total = custo_singlegrafos + custo_subgrafos
custo_total = custo_singlegrafos + custo_subgrafos

print("O custo total é",custo_total)
