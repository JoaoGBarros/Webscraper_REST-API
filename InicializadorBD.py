import requests

BASE = "http://127.0.0.1:5000/"
data = [{"nome": "Mercado Livre",
         "pesquisa": "nav-search-input",
         "link": "https://www.mercadolivre.com.br/",
         "classe_conteudo": "ui-search-result__wrapper",
         "tag_conteudo": "div",
         "classe_titulo": "ui-search-item__group ui-search-item__group--title",
         "tag_titulo": "div",
         "classe_links": "ui-search-link",
         "tag_links": "a",
         "classe_preco": "price-tag-amount",
         "tag_preco": "span",
         "classe_frete": "ui-search-item__shipping ui-search-item__shipping--free",
         "tag_frete": "p",
         "classe_procura_prox_pag": "ui-search-pagination",
         "tag_procura_prox_pag": "div",
         "classe_proxima": "andes-pagination__link ui-search-link",
         "tag_proxima": "a",
         "titulo": "Seguinte"
         },
        {"nome": "Amazon",
         "pesquisa": "twotabsearchtextbox",
         "link": "https://www.amazon.com.br/",
         "classe_conteudo": "a-section a-spacing-medium",
         "tag_conteudo": "div",
         "classe_titulo": "a-size-base-plus a-color-base a-text-normal",
         "tag_titulo": "span",
         "classe_links": "a-link-normal a-text-normal",
         "tag_links": "a",
         "classe_preco": "a-offscreen",
         "tag_preco": "span",
         "classe_frete": "a-row",
         "tag_frete": "span",
         "classe_procura_prox_pag": "a-last",
         "tag_procura_prox_pag": "li",
         "classe_proxima": "",
         "tag_proxima": "a",
         "titulo": ""
         }]

for i in range(len(data)):
    response = requests.put(BASE + "loja/" + str(i), data[i])
    print(response.json())

input()
response = requests.get(BASE + "loja/0")
print(response.json())
