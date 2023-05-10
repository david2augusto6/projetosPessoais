function fatorial(n){
    let fat = 1
    for(var c=n; c > 1; c--){
        fat *=c
    }
    return fat
}

/*function fatorial(n){ // função recursiva
    if (n==1){
        return 1
    }else{
    return n*fatorial(n-1)
    }
}*/

console.log(fatorial(21))