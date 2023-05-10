#include <stdio.h>

int soma(int a, int b){
    return a + b;
}

int dobro(int a){
    return 2*a;
}

main(){
    int n, i , tot;
    printf("Insira dois numeros:");scanf("%d%d", &n, &i);
    tot = soma(n, i);
    printf("%d + %d = %d\n", n, i, tot);
    printf("2*%d = %d e 2*%d=%d\n", n, dobro(n), i, dobro(i));
}