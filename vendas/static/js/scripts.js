//Objeto que guarda vários elementos do site
const elements = {
    botao: document.querySelector('.switch'),
    head: document.querySelector('header'),
    title: document.querySelector('h1'),
    checkbox: document.getElementById('mode'),
    body: document.querySelector('body'),
    footer: document.querySelector('footer'),
    salvar: document.querySelector('button'),
    titulo_list: document.querySelector('.titulo'),
    barra: document.querySelector('.busca'),
    sub_tit: document.querySelector('h3'),
    busca: document.querySelector('.buscar'),
    tabela: document.querySelector('.tabela'),
    t_head: document.querySelector('.title-table'),

    backButton: document.querySelector('.back'),
    logo: document.querySelector('.Logo_D'),
    logoSol: document.querySelector('.sol'),
    logoLua: document.querySelector('.lua'),
    logoReg: document.querySelector('.reg'),
    logoCons: document.querySelector('.cons'),
    logoRelat: document.querySelector('.relat'),
    logoVenda: document.querySelector('.venda'),
    logoRegis: document.querySelector('.regis'),
    logoProd: document.querySelector('.prod'),
    logoSell: document.querySelector('.sell')
}

//Lista de elementos com o mesmo nome
const links = document.querySelectorAll('.links')
const creators = document.querySelectorAll('.github')
const textForm = document.querySelectorAll('.texto')
const entradas = document.querySelectorAll('input')
const selection = document.querySelectorAll('select')
const searchs = document.querySelectorAll('.search')
const itens = document.querySelectorAll('.itens')
const produtos = document.querySelectorAll('.produto')
const infos = document.querySelectorAll('.infos')
const dados = document.querySelectorAll('td')

//Função que verifica o tema atual do site
function verifyTheme() {
    //verifica se o tema salvo atualmente está guardado no banco de dados do navegador
    const temaSalvo = localStorage.getItem('tema')

    //Verifica se o botão está ativo no modo escuro ou não
    if (temaSalvo === 'escuro') {
        if (elements.checkbox) { 
            elements.checkbox.checked = true
            mudarTema(true)
        }
    } else {
        if (elements.checkbox) {
            elements.checkbox.checked = false
            mudarTema(false)
        }
    }
}

//Adiciona evento ao clicar no botão de modo
//Dentro de EventListener, pode-se usar function ou usar () =>
if (elements.botao) {
    elements.botao.addEventListener('click', function verify() {
        const newState = !elements.body.classList.contains('dark_body')
        
        //Verifica o estado atual do site
        let temaText
        if (newState === true) {
            temaText = 'escuro'
        } else {
            temaText = 'claro'
        }

        //Outra forma de usar o newState
        //localStorage.setItem('tema', newState ? 'escuro' : 'claro')
        localStorage.setItem('tema', temaText)
        mudarTema(newState)
    })
}


//Função que centraliza as mudanças na tela
function mudarTema(isDark) {
    //Alterações de cor no modo escuro
    if (elements.title) elements.title.classList.toggle('dark_mode',isDark)
    if (elements.head) elements.head.classList.toggle('light_head',isDark)
    if (elements.body) elements.body.classList.toggle('dark_body',isDark)
    if (elements.footer) elements.footer.classList.toggle('light_footer',isDark)
    if (elements.backButton) elements.backButton.classList.toggle('dark_back', isDark)
    if (elements.salvar) elements.salvar.classList.toggle('button_dark')
    if (elements.titulo_list) elements.titulo_list.classList.toggle('dark_title', isDark)
    if (elements.barra) elements.barra.classList.toggle('busca_dark', isDark)
    if (elements.sub_tit) elements.sub_tit.classList.toggle('sub_dark', isDark)
    if (elements.busca) elements.busca.classList.toggle('dark_buscar', isDark)
    if (elements.t_head) elements.t_head.classList.toggle('title-table_dark', isDark)
    if (elements.tabela) elements.tabela.classList.toggle('tabela_dark', isDark)
    //Verifica se os links estão no modo escuro ou não
    if (isDark) {
        links.forEach(link => link.classList.add('link_dark'))
        creators.forEach(creator => creator.classList.add('git_dark'))
        textForm.forEach(texto => texto.classList.add('texto_dark'))
        entradas.forEach(enter => enter.classList.add('enter_dark'))
        selection.forEach(select => select.classList.add('enter_dark'))
        searchs.forEach(search => search.classList.add('search_dark'))
        itens.forEach(item => item.classList.add('itens_dark'))
        produtos.forEach(produto => produto.classList.add('produto_dark'))
        infos.forEach(info => info.classList.add('infos_dark'))
        dados.forEach(dado => dado.classList.add('dados_dark'))
        //Chama as imagens de modo escuro
        darkMode()
    } else {
        links.forEach(link => link.classList.remove('link_dark'))
        creators.forEach(creator => creator.classList.remove('git_dark'))
        textForm.forEach(texto => texto.classList.remove('texto_dark'))
        entradas.forEach(enter => enter.classList.remove('enter_dark'))
        selection.forEach(select => select.classList.remove('enter_dark'))
        searchs.forEach(search => search.classList.remove('search_dark'))
        itens.forEach(item => item.classList.remove('itens_dark'))
         produtos.forEach(produto => produto.classList.remove('produto_dark'))
        infos.forEach(info => info.classList.remove('infos_dark'))
        dados.forEach(dado => dado.classList.remove('dados_dark'))
        //Chama as imagens de modo claro
        lightMode()
    }

}

//Função para trocar imagens para o modo claro
function lightMode() {
    if (elements.logo) elements.logo.src = "../../static/img/letra-d.png"
    if (elements.logoSol) elements.logoSol.src = "../../static/img/sun.png"
    if (elements.logoLua) elements.logoLua.src = "../../static/img/lua-crescente.png"
    if (elements.logoReg) elements.logoReg.src = "../../static/img/editar.png"
    if (elements.logoCons) elements.logoCons.src = "../../static/img/pesquisa-de-lupa.png"
    if (elements.logoRelat) elements.logoRelat.src = "../../static/img/relatorio.png"
    if (elements.logoVenda) elements.logoVenda.src = "../../static/img/carrinho.png"
    if (elements.logoRegis) elements.logoRegis.src = "../../static/img/registro.png"
    if (elements.logoProd) elements.logoProd.src = "../../static/img/produtos.png"
    if (elements.logoSell) elements.logoSell.src = "../../static/img/venda.png"
}

//Função para trocar imagens para o modo escuro
function darkMode() {
    if (elements.logo) elements.logo.src = "../../static/img/letra-d-dark.png"
    if (elements.logoSol) elements.logoSol.src = "../../static/img/sun-dark.png"
    if (elements.logoLua) elements.logoLua.src = "../../static/img/lua-crescente-dark.png"
    if (elements.logoReg) elements.logoReg.src = "../../static/img/editar-dark.png"
    if (elements.logoCons) elements.logoCons.src = "../../static/img/pesquisa-de-lupa-dark.png"
    if (elements.logoRelat) elements.logoRelat.src = "../../static/img/relatorio-dark.png"
    if (elements.logoVenda) elements.logoVenda.src = "../../static/img/carrinho-dark.png"
    if (elements.logoRegis) elements.logoRegis.src = "../../static/img/registro-dark.png"
    if (elements.logoProd) elements.logoProd.src = "../../static/img/produtos-dark.png"
    if (elements.logoSell) elements.logoSell.src = "../../static/img/venda-dark.png"
}

//Chama a função para verificar o tema do site
verifyTheme()