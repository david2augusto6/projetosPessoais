#include <stdio.h>

float pot(float x, int p){
    float res;int i;
    for(i=1,res=1.0 ; i <=p; i++){
        res *= x;
    }
    return res;
}

float val(float x, int n, float t){
    float val;int c;

    for(val=0,c=1; c <= n; c++)
    {
    val = val + x / pot((1+t), c);
    }
    return val;
}


main(){
    printf("%f\n", pot(2.0, 4));
    printf("val = %f", val(5.0, 3, 0.3));
}