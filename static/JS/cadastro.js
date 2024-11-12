const tipoCadastro = document.querySelector("#tipoCadastro");
const cadastroPais = document.querySelector("#cadastroPais");
const cadastroadministracao = document.querySelector("#cadastroadministracao");

tipoCadastro.addEventListener('submit', (event) => {
    event.preventDefault();
    const selecionarTipoCadastro = document.querySelector("#selecionarTipoCadastro").value;
    if (selecionarTipoCadastro === 'Pais') {
        cadastroPais.style.display = 'block';
        cadastroadministracao.style.display = 'none';
        cadastroPais.scrollIntoView({behavior: 'smooth'})
    }else{
        cadastroPais.style.display = 'none';
        cadastroadministracao.style.display = 'block';
        cadastroadministracao.scrollIntoView({behavior: 'smooth'})
    }
} )

cadastroadministracao.addEventListener('submit', (event) =>{
    event.preventDefault();
    let senha = document.querySelector("#senhaadministracao");
    let repetirsenha = document.querySelector("#repetirsenhaadministracao");
    let msgErro = document.querySelector("#msgErroadministracao");

    if (senha.value !== repetirsenha.value) {
        msgErro.style.display = 'block';
        repetirsenha.style.background = 'red';
        senha.style.background = 'red';
        return false;
    }else{
        msgErro.style.display = 'none';
        repetirsenha.style.background = 'white';
        senha.style.background = 'white';
        cadastroadministracao.submit();
        return true;
    }
})

cadastroPais.addEventListener('submit', (event) =>{
    event.preventDefault();
    let senha = document.querySelector("#senhaPais");
    let repetirsenha = document.querySelector("#repetirsenhaPais");
    let msgErro = document.querySelector("#msgErroPais");

    if (senha.value !== repetirsenha.value) {
        msgErro.style.display = 'block';
        repetirsenha.style.background = 'red';
        senha.style.background = 'red';
        return false;
    }else{
        msgErro.style.display = 'none';
        repetirsenha.style.background = 'white';
        senha.style.background = 'white';
        cadastroPais.submit();
        return true;
    }
})