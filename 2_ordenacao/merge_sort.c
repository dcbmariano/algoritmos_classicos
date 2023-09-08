#include <stdio.h>
/* 
*  MergeSort
*  logica:  divide array em 2 recursivamente até n>1
*           depois chama a funcao merge para mesclar as listas
*  retorna: array ordenado
*  custo:   O(n lg n)
*/ 

int merge(int A[], int ini, int meio, int fim){
    
    int i, j, k;
    int n1 = meio-ini+1, n2 = fim-meio;  // tam. arrays temp.

    int tmp1[n1], tmp2[n2]; // 2 arrays temporarios
    
    // preenche os arrays temporario
    for(i=0; i<n1; i++) tmp1[i] = A[ini+i];
    for(i=0; i<n2; i++) tmp2[i] = A[meio+1+i];

    // ordena vetor A
    i = 0; j = 0; k = ini;
    while( (i < n1) && (j < n2) ){
        if (tmp1[i] <= tmp2[j]) {
            A[k] = tmp1[i]; i++;
        } else {
            A[k] = tmp2[j]; j++;
        }

        k++;
    }

    // se sobrou algum elemento, adiciona ele em A
    while(i<n1){ A[k] = tmp1[i]; i++; k++; }
    while(j<n2){ A[k] = tmp2[j]; j++; k++; }

    return 0;
}

int divide(int A[], int ini, int fim){
    
    if(ini >= fim) return 0; // caso base

    int meio = (ini + fim)/2; // piso: arredonda pra baixo se impar
    
    divide(A, ini, meio);     // custo: lg(n)
    divide(A, meio+1, fim);   // custo: lg(n)
    merge(A, ini, meio, fim); // custo: n

    return 0;
}

int merge_sort(void){
    // custo total: n lg n

    int chave, i, j, n;
    int A[] = {7, 1, 2, 9, 4, 3, 5, 0};
    n = sizeof(A)/sizeof(A[0]);  
    //printf("Tamanho de n é %d\n", n);

    int B[n]; // vetor ordenado vazio

    printf("Vetor original: ");
    for(i=0; i<n; i++) printf("%d, ",A[i]);

    // INICIA A DIVISÃO E CONQUISTA
    divide(A, 0, n);

    printf("\nVetor ordenado: ");
    for(i=0; i<n; i++) printf("%d, ",A[i]);

    return 0;
}

int main(void){
    merge_sort();
    return 0;
}