function gerarTabuada(){
    var num = document.getElementById("txtnum")
    var resTabuada = document.getElementById("tab")
    

    if (num.value.length == 0){
        alert("[ERRO] Faltam dados")
    } else{
        var n = Number(num.value)

        for (var c = 0; c <= 10; c++){
            let item = document.createElement('option')
            item.text = `${n} x ${c} = ${n*c}`
            item.value = `tab${c}`
            resTabuada.appendChild(item)
        }
        resTabuada.innerHTML = ""
    }
}