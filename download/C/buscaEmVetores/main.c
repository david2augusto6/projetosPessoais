#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#include "vetor.c"

int main(){
    VETOR *v;
    int buscar;
    v = Criar_vetor(10);
    printf("\nQuantidade de elementos: %d", v->qtd);
    Inserir_elementos(v);
    Print_elementos(*v);


    printf("\nValor que deseja buscar: ");scanf("%d", &buscar);

    printf("Resultado da busca = %d", Busca_Sequencia(v, buscar));
    libera(v);
    return 0;
}