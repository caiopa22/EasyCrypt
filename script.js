var btnEntrar = document.querySelector("#entrar")
var btnSair = document.querySelector("#sair")

var body = document.querySelector("body");

btnEntrar.addEventListener("click", function() {
    body.className = "entrar-js"
});

btnSair.addEventListener("click", function() {
    body.className = "sair-js"
});


function mostrarSenhaPrimary(){
    var inputPassPrimary = document.getElementById('encrypted-message-primary')
    var btnShowPassPrimary = document.getElementById('btn-encrypted-message-primary')

    if(inputPassPrimary.type === 'password'){
        inputPassPrimary.setAttribute('type','text')
        btnShowPassPrimary.classList.replace('bi-eye-fill','bi-eye-slash-fill')
    }else if(inputPassPrimary.type === 'text'){
        inputPassPrimary.setAttribute('type','password')
        btnShowPassPrimary.classList.replace('bi-eye-slash-fill','bi-eye-fill')
    }
}

function mostrarSenhaSecond(){
    var inputPassSecond = document.getElementById('decrypted-message')
    var btnShowPassSecond = document.getElementById('btn-decrypted-message')

    if(inputPassSecond.type === 'password'){
        inputPassSecond.setAttribute('type','text')
        btnShowPassSecond.classList.replace('bi-eye-fill','bi-eye-slash-fill')
    }else if(inputPassSecond.type === 'text'){
        inputPassSecond.setAttribute('type','password')
        btnShowPassSecond.classList.replace('bi-eye-slash-fill','bi-eye-fill')
    } 
}


function btnInfoEnter(){
    var btnInformacoes = document.getElementById('btnInformacoes') 
    var btnInfo = document.getElementById('informacoes')
    var circulo = document.getElementsByClassName('bi-info-circle')
    

    if(btnInfo.type === 'password'){
        btnInfo.setAttribute('type','text')
        btnInformacoes.classList.replace('bi-info-circle','bi-info-circle-fill')
    }else if(btnInfo.type === 'text'){
        btnInfo.setAttribute('type','password')
        btnInformacoes.classList.replace('bi-info-circle-fill','bi-info-circle')
    } 
}


