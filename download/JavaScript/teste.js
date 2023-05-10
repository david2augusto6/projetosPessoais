function maior(lista){
    let maior = 0
    for(var e in lista){
        if (e==0){
            maior = lista[e]
        }else if (maior < lista[e]){
            maior = lista[e]
        }
    }
    return maior
}

function menor(lista){
    let menor = 0
    for(var e in lista){
        if (e==0){
            menor = lista[e]
        }else if (menor > lista[e]){
            menor = lista[e]
        }
    }
    return menor
}

function soma(lista){
    let s = 0
    for (var c in lista){
        s += lista[c]
    }
    return s
}

function média(lista){
    let m = soma(lista)/lista.length
    return m
}

l = [4,3,2,6]
console.log(maior(l))
console.log(menor(l))

console.log(soma(l))
console.log(média(l))