import requests
from web_scraper_geral import Busca
import pandas as pd
import os


def EscohaLoja(lojas):
    while True:
        print("Em que site de compras deseja procurar: ")
        print("1 - Mercado Livre")
        print("2 - Amazon")

        opcao = int(input())

        if opcao in lojas:
            print("Tente novamente")
        else:
            lojas.append(opcao-1)
            break

    return opcao-1


if __name__ == '__main__':

    BASE = "http://127.0.0.1:5000/"
    print("------- Servico de Busca Automatizada -------")
    produto = input("Produto que deseja buscar: ")
    arquivo = input("Nome do arquivo que sera gerado: ")
    arquivo = arquivo + '.csv'
    on = True
    lista_links = []  # Vetor de links dos produtos
    lista_titulos = []  # Vetor com o titulo dos anuncios
    lista_precos = []  # Vetor com os precos
    lista_fretes = []  # Vetor com os fretes
    lista_lojas = []
    lojas = []
    lojas_vistas = []
    contador = 0
    if not os.path.exists("Relatorios"):
        os.mkdir("Relatorios")
    arquivo = os.getcwd() + "/Relatorios/" + arquivo
    while on:
        op = EscohaLoja(lojas)
        link = BASE + "loja/" + str(op)
        response = requests.get(BASE + "loja/" + str(op))
        info = response.json()
        Busca(info, produto, arquivo, lista_links, lista_titulos, lista_precos, lista_fretes, lista_lojas)

        print("Deseja adicionar outra loja na tabela?\n1-Sim\n2-Nao\n")
        escolha = int(input())
        if escolha == 2:
            data = pd.DataFrame(zip(lista_precos, lista_titulos, lista_lojas, lista_fretes, lista_links), columns=['Preco', 'Produto', 'Loja', 'Frete', 'Link'])
            data.to_csv(arquivo, index=False, encoding='utf-8')
            on = False



    
    print("Fim do programa! O .csv esta disponivel em " + arquivo + "!")
