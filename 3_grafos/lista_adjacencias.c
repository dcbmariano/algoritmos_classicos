// Cria lista de adjacências
// Entrada: par de vértices
// Saída: lista de adjacências
// Executar:
// gcc lista_adjacencias.c -o lista_adjacencias && ./lista_adjacencias < grafo_1
#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

// estruturas de dados que armazenam a lista de adjacencias
struct Vertice{ int destino; struct Vertice* proximo; };
struct Lista{ struct Vertice* cabecalho; };

struct Vertice* cria_vertice(int destino){
    struct Vertice* novo = (struct Vertice*)malloc(sizeof(struct Vertice));
    novo->proximo = NULL; novo->destino = destino;
    return novo;
}

struct Lista* geraGrafo(int n){
    struct Lista* grafo = (struct Lista*)malloc(sizeof(struct Lista) * n);
    int i = 1;
    while(i<=n){ grafo[i].cabecalho = NULL; i++; }
    return grafo;
}

int add_aresta(struct Lista* grafo, int origem, int destino){
    // adiciona uma aresta no grafo

    struct Vertice* novo = cria_vertice(destino);
    novo->proximo = grafo[origem].cabecalho;
    grafo[origem].cabecalho = novo;
    return 0;
}

int imprimir(struct Lista* grafo, int n){
    // imprime o grafo

    int i = 1;
    while(i<=n){
        struct Vertice* atual = grafo[i].cabecalho;
        printf("Vertice %d: ", i);

        while(atual != NULL){
            printf("%d => ", atual->destino);
            atual = atual->proximo;
        }
        if(atual == NULL) printf("NULL\n"); // fim da lista
        i++;
    }
    return 0;
}

int main(void){
    // função principal

    int i, j, old_i, old_j, cont = 0, n = 5;
    struct Lista* grafo = geraGrafo(n);
    bool sair = false;

    while(!sair){

        scanf("%d %d", &i, &j);

        if((i == old_i)&&(j == old_j)) break;
        else old_i = i; old_j = j; 
        
        add_aresta(grafo, i, j);

    }

    imprimir(grafo, n);
    
    return 0;
}