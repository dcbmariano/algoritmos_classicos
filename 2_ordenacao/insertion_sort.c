#include <stdio.h>

int insertion_sort(void){

    const int n = 8;
    int chave, i, j;
    int A[n] = {7, 1, 2, 9, 4, 3, 5, 0};

    printf("Vetor original: ");
    for(i=0; i<n; i++) printf("%d, ",A[i]);

    // ORDENAÇÃO POR INSERÇÃO
    // laço externo
    for(i=1; i<n; i++){
        chave = A[i];
        j = i-1;

        // laço interno
        while((j>=0)&&(A[j]>chave)){
            A[j+1] = A[j];
            j--;
        }

        A[j+1] = chave;
        
    }

    // imprimindo o vetor ordenado
    printf("\nVetor ordenado: ");
    for(i=0; i<n; i++) printf("%d, ", A[i]);

    return 0;
}

int main(void){
    insertion_sort();

    return 0;
}