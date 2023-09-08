#include <stdio.h>

int selection_sort(void){
    
    const int n = 8;
    int A[n] = {7, 1, 2, 9, 4, 3, 5, 0};
    int menor, i, j, aux; 

    printf("\nVetor original: ");
    for(i=0; i<n; i++) printf("%d, ", A[i]);

    // ORDENANDO O VETOR
    // laço externo
    for(i=0; i<n-1; i++){
        menor = A[i];
        aux = i;
        //printf("\ni=%d - j=",A[i]);
        // laço interno
        for(j=i+1; j<n; j++){
            //printf("%d,",A[j]);
            if(A[j] < menor){
                menor = A[j];
                aux = j;
            }
        }

        // troca
        A[aux] = A[i];
        A[i] = menor;
        // printf("MENOR=%d",menor);

    }

    // imprimindo o vetor ordenado
    printf("\nVetor ordenado: ");
    for(i=0; i<n; i++) printf("%d, ", A[i]);

    return 0;

}

int main(void){
    selection_sort();
    return 0;
}
