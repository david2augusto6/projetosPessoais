#include <stdio.h>
#include <stdlib.h>
#include <conio.h>
#include "vetor.h"

VETOR* Criar_vetor(int qtd){
    VETOR* out = malloc(sizeof(VETOR));
    out->elem = malloc(qtd * sizeof(int));
    out->qtd = qtd;
    return out;
}

void libera(VETOR *v){
    free(v->elem);
    free(v);
}

void Inserir_elementos(VETOR *v){
    int i, s;
    s = rand()%100;
    printf("\n");
    for (i=0; i<v->qtd; i++){
        v->elem[i] = s * rand()%100;
    }
}

void Print_elementos(VETOR v){
    int i;
    printf("\n--------Elementos no vetor--------\n");
    printf("%s%12s\n", "Posicao", "Valor");
    for(i=0; i<v.qtd; i++){
        printf("%7d%12d\n", i+1, v.elem[i]);
    }
}

int Busca_Sequencia(VETOR* v, int k){
    int i;
    for(i=0; i < v->qtd; i++){
        if (v->elem[i]==k){
            return i+1;
        }
    }
    return -1;
}