let num = document.querySelector("input#txtnum")
let lista = document.querySelector("select#lista")
let res = document.querySelector("div#res")
let valores = []

function isNumero(n){
    if (Number(n) >=1 && Number(n) <=100){
        return true
    }else{
        return false
    }
}

function inLista(n, lista){
    if (lista.indexOf(Number(n)) != -1){
        return true
    }else{
        return false
    }
}

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

function adicionar(){
    if (isNumero(num.value) && !inLista(num.value, valores)){
        var c = Number(num.value)
        var item = document.createElement("option")
        item.text = `Valor ${c} foi adicionado`
        item.value = `lista${c}`
        lista.appendChild(item)
        valores.push(c)
    }else{
        alert("Valor inválido ou já existente")
    }
    num.value = ''
    num.focus()
}

function finalizar(){
    if (valores.length == 0){
        alert("Adicione valores para finalizar!!!")
    }else{
        res.innerHTML += `<p>Ao todo, temos ${valores.length} valores cadastrados.</p>`
        res.innerHTML += `<p>O <strong>maior</strong> elemento é ${maior(valores)}.</p>`
        res.innerHTML += `<p>O <strong>menor</strong> elemento é ${menor(valores)}.</p>`
        res.innerHTML += `<p>A <strong>soma</strong> dos elementos é ${soma(valores)}.</p>`
        res.innerHTML += `<p>A <strong>média</strong> dos elementos é ${média(valores)}.</p>`
    }
}