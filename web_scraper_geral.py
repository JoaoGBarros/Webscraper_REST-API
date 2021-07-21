from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import os


def produtoCerto(produto_encontrado, produto_procurado):

    #  Funcao que compara o titulo do anuncio encontrado com o produto procurado. Caso todas as palavras do produto
    # procurado estejam presentes, retorna True, caso nao, retorna False
    produto_procurado = produto_procurado.lower()
    produto_encontrado = produto_encontrado.lower()
    soma = 0
    for i in range(len(produto_procurado)):
        if produto_procurado[i] in produto_encontrado:
            soma += 1

    if soma == len(produto_procurado):
        return True
    else:
        return False


def Busca(info, produto, arquivo, lista_links, lista_titulos, lista_precos, lista_fretes, lista_lojas):

    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    existe_proxima = True  # Inicia a condicao para o loop

    # Pega o path da pasta em que o programa esta sendo executado
    local = os.getcwd()
    local = local + "/chromedriver.exe"  # Inclui o executavel do chrome driver no path
    print("Espere a janela do Chrome fechar para abrir o arquivo .csv")
    navegador = webdriver.Chrome(local, options=options)   # Abre o executavel do chrome driver
    navegador.minimize_window()
    site = info['link']
    navegador.get(site)  #Entra no site

    # Procura pelo elemento da barra de pesquisa utilizando sua classe no html
    if 'amazon' in site or 'americanas' in site:
        pesquisa = navegador.find_element_by_id(info['pesquisa'])
    else:
        pesquisa = navegador.find_element_by_class_name(info['pesquisa'])


    pesquisa.send_keys(produto)  # Digita na barra de pesquisa o produto
    pesquisa.send_keys(Keys.RETURN)  # ENTER

    # Espera 5 segundos antes de comecar a coleta de dados para dar tempo da pagina carregar completamente

    navegador.implicitly_wait(5)
    conteudo = navegador.page_source


    # Cria um novo objeto de BeautifulSoup contendo as informacoes da pagina
    soup = BeautifulSoup(conteudo, features="html.parser")

    while existe_proxima:
        proxima = None  # Inicializa a verificacao para caso exista uma proxima pagina
        #  Faz a busca dentro da div que possua a classe especificada
        for a in soup.find_all(info['tag_conteudo'], attrs={'class': info['classe_conteudo']}):
            # a.find -> De todos os elementos presentes dentro da div, procura os com as especificacoes
            nome = a.find(info['tag_titulo'], attrs={'class': info['classe_titulo']})
            if produtoCerto(nome.text, produto):
                #  Caso a condicao seja verdadeira, armazena os dados do anuncio

                link = a.find(info['tag_links'], attrs={'class': info['classe_links']})
                preco = a.find(info['tag_preco'], attrs={'class': info['classe_preco']})
                frete = a.find(info['tag_frete'], attrs={'class': info['classe_frete']})
                if not isinstance(preco, type(None)):
                    if "click" not in link.attrs['href']:
                        if site not in link.attrs['href']:
                            link.attrs['href'] = site + link.attrs['href']
                        lista_links.append(link.attrs['href'])
                    lista_titulos.append(nome.text)
                    lista_precos.append(preco.text)
                    lista_lojas.append(info['nome'])
                    if isinstance(frete, type(None)):
                        lista_fretes.append("Sem fretis gratis")
                    else:
                        lista_fretes.append(frete.text)

        #  Procura pelo botao para mudar de pagina, seguindo apenas para proximas paginas
        for a in soup.find_all(info['tag_procura_prox_pag'], attrs={'class': info['classe_procura_prox_pag']}):
            proxima = a.find(info['tag_proxima'], attrs={'class': info['classe_proxima'], 'title': info['titulo']})


        # Caso a proxima pagina nao exista, o loop eh finalizado
        if isinstance(proxima, type(None)):
            existe_proxima = False
            navegador.quit()  #Fecha o navegador
        else:
            # Caso contrario o programa carrega a proxima pagina
            if 'amazon' in site:
                site = site + proxima.attrs['href']
            else:
                site = proxima.attrs['href']
            navegador.get(site)
            conteudo = navegador.page_source
            soup = BeautifulSoup(conteudo, features="html.parser")

