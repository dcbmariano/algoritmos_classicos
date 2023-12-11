def dfs(u, visited, adj_list):
    visited[u] = True
    for v in adj_list[u]:
        if not visited[v]:
            dfs(v, visited, adj_list)

n = 6 # número de vértices
edges = [(1,2), (1,3), (2,3), (4,5)] # lista de arestas

# construindo lista de adjacência
adj_list = [[] for i in range(n)]
for u, v in edges:
    adj_list[u-1].append(v-1)
    adj_list[v-1].append(u-1)

# realizando busca em profundidade a partir do vértice 0
visited = [False]*n
dfs(0, visited, adj_list)

# verificando se todos os vértices foram alcançáveis
if all(visited):
    print("Grafo conectado")
else:
    print("Grafo não conectado")