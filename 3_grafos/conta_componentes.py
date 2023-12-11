# contagem de componentes com busca em profundidade 

G = {
	0: [1, 2],
	1: [0],
	2: [0],
	3: [4,5],
	4: [3],
	5: [3],
	6: [7],
	7: [6]
}

descoberta = []
termino = []
pai = []
cor = []
inf = float("inf")
tempo = 0
comp = 0


def inicializa_fonte(G):
	for v in G:
		descoberta.append(inf)
		termino.append(inf)
		pai.append(-1)
		cor.append('branco')

inicializa_fonte(G)

def busca_em_profundidade(G, s):
	global tempo
	descoberta[s] = tempo 
	for vizinho in G[s]:
		if cor[vizinho] == "branco":
			cor[vizinho] = "cinza"
			busca_em_profundidade(G, vizinho)
	tempo += 1
	termino[s] = tempo
	cor[s] = tempo

def conta_componentes(G):
	global comp
	for v in G:
		if cor[v] == "branco":
			comp += 1
			busca_em_profundidade(G, v)


	print("A quantidade de componentes é", comp)

conta_componentes(G)
