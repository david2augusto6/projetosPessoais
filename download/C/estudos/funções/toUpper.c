#include <stdio.h>

int toUpper(char c){
    if (c >= 'a' && c <= 'z')
        return c + 'A' - 'a';
    else
        return c;
}


main(){
    char c;
    while (1){
        c=getchar();
        putchar(toUpper(c));
    }
}
