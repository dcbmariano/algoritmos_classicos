# Um programa Python3 para verificar se um grafo contém 
# ciclo de peso negativo usando o algoritmo de Bellman-Ford. 

class Aresta:     
    def __init__(self):
        self.origem = 0
        self.prox = 0
        self.peso = 0
 
class Grafo:
    def __init__(self):
        self.V = 0
        self.E = 0
        self.aresta = None
 
def criaGrafo(V, E):
    grafo = Grafo()
    grafo.V = V;
    grafo.E = E;
    grafo.aresta =[Aresta() for i in range(grafo.E)]
    return grafo
 
# The main function that finds shortest distances
# from origem to all other vertices using Bellman-
# Ford algorithm.  The function also detects
# negative peso cycle
def temCicloNegativo(grafo, origem):
 
    V = grafo.V;
    E = grafo.E;
    dist = [1000000 for i in range(V)];
    dist[origem] = 0;
 
    # Step 2: Relax all arestas |V| - 1 times.
    # A simple shortest path from origem to any
    # other vertex can have at-most |V| - 1
    # arestas
    for i in range(1, V):
        for j in range(E):
         
            u = grafo.aresta[j].origem;
            v = grafo.aresta[j].prox;
            peso = grafo.aresta[j].peso;
            if (dist[u] != 1000000 and dist[u] + peso < dist[v]):
                dist[v] = dist[u] + peso;
 
    # Step 3: check for negative-peso cycles.
    # The above step guarantees shortest distances
    # if grafo doesn't contain negative peso cycle.
    # If we get a shorter path, then there
    # is a cycle.
    for i in range(E):
     
        u = grafo.aresta[i].origem;
        v = grafo.aresta[i].prox;
        peso = grafo.aresta[i].peso;
        if (dist[u] != 1000000 and dist[u] + peso < dist[v]):
            return True;
 
    return False;

 
if __name__=='__main__':
     
    V = 5; # Number of vertices in grafo
    E = 8; # Number of arestas in grafo
    grafo = criaGrafo(V, E);
 
    # add aresta 0-1 (or A-B in above figure)
    grafo.aresta[0].origem = 0;
    grafo.aresta[0].prox = 1;
    grafo.aresta[0].peso = -1;
 
    # add aresta 0-2 (or A-C in above figure)
    grafo.aresta[1].origem = 0;
    grafo.aresta[1].prox = 2;
    grafo.aresta[1].peso = 4;
 
    # add aresta 1-2 (or B-C in above figure)
    grafo.aresta[2].origem = 1;
    grafo.aresta[2].prox = 2;
    grafo.aresta[2].peso = 3;
 
    # add aresta 1-3 (or B-D in above figure)
    grafo.aresta[3].origem = 1;
    grafo.aresta[3].prox = 3;
    grafo.aresta[3].peso = 2;
 
    # add aresta 1-4 (or A-E in above figure)
    grafo.aresta[4].origem = 1;
    grafo.aresta[4].prox = 4;
    grafo.aresta[4].peso = 2;
 
    # add aresta 3-2 (or D-C in above figure)
    grafo.aresta[5].origem = 3;
    grafo.aresta[5].prox = 2;
    grafo.aresta[5].peso = 5;
 
    # add aresta 3-1 (or D-B in above figure)
    grafo.aresta[6].origem = 3;
    grafo.aresta[6].prox = 1;
    grafo.aresta[6].peso = 1;
 
    # add aresta 4-3 (or E-D in above figure)
    grafo.aresta[7].origem = 4;
    grafo.aresta[7].prox = 3;
    grafo.aresta[7].peso = -3;

    # grafo.aresta[8].origem = 3;
    # grafo.aresta[8].prox = 4;
    # grafo.aresta[8].peso = -3;
 
    if (temCicloNegativo(grafo, 0)):
        print("Sim")
    else:
        print("Não")
 