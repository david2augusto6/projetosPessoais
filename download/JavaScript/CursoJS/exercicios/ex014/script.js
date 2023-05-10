function carregar(){
    var msg = window.document.getElementById("msg")
    var img = window.document.getElementById("imagem")
    var data = new Date()
    //var hora = data.getHours()
    var hora = 19
    msg.innerHTML = `Agora são ${hora} horas.`
    if (hora >= 0 && hora < 12){
        // bom dia
        img.src = 'manhã.png'
        document.body.style.background = "#fdde5f"
    } else if (hora >= 12 && hora < 18){
        //boa tarde
        img.src = 'tarde.png'
        document.body.style.background = "#6887a6"
    }else{
        //boa noite
        img.src = 'noite.png'
        document.body.style.background = "#07387a"
    }
}