function verificar(){
    var data = new Date()
    var ano = data.getFullYear()
    var fano = document.getElementById("txtano")
    var res = document.getElementById("res")
    if (fano.value.length == 0 || fano.value > ano){
        window.alert("ERRO! Verifique os dados e tente novamente")
    }else{
        var fsexo = document.getElementsByName("radsex")
        var idade = ano - Number(fano.value)
        var sexo = ''
        var img = document.createElement('img')
        img.setAttribute("id", "foto")
        if (fsexo[0].checked){
            sexo = "Homem"
            if (idade >=0 && idade < 12){
                //criança
                img.setAttribute("src","menino.png")
            }else if (idade >= 12 && idade < 21){
                // jovem
                img.setAttribute("src", "jovem-h.png")
            }else if (idade < 50){
                // adulto
                img.setAttribute("src", "adulto.png")
            }else{
                // idoso
                img.setAttribute("src", "idoso.png")
            }
        } else if (fsexo[1].checked){
            sexo = "Mulher"
            if (idade >=0 && idade < 12){
                //criança
                img.setAttribute("src", "menina.png")
            }else if (idade >= 12 && idade < 21){
                // jovem
                img.setAttribute("src", "jovem-m.png")
            }else if (idade < 50){
                // adulto
                img.setAttribute("src", "adulta.png")
            }else{
                // idoso
                img.setAttribute("src", "idosa.png")
            }
        }
        res.style.textAlign = 'center'
        res.innerHTML = `Detectamos ${sexo} com ${idade} anos.`
        res.appendChild(img)
    }
}