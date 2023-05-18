#ifndef VETOR_H_INCLUDED
#define VETOR_H_INCLUDED

typedef struct{
	int *elem;
	int qtd;
}VETOR;

VETOR * Cria_Vetor(int qtd);
void Inserir_elementos(VETOR *v);
void Print_elementos(VETOR v);
void Busca_sequencia(VETOR *v, int k);

#endif