import requests
url_children = []


def crawler(url_inicial, depth=2, max_paginas=10):
    print(f"Começando com a URL {url_inicial}")
    visitados=[]
    url_parents = [url_inicial]
    global url_children
    index = 0
    while depth >= index and len(visitados)< max_paginas:
        for url_pai in url_parents:
            if url_pai not in visitados:
                buscar_todos_links(url_pai)
                visitados.append(url_pai)
                print(f"Visitando {url_pai}. depth: {index}")
            if max_paginas <= len(visitados):
                print("Visitado o máximo de páginas")
                break
        url_parents = url_children
        url_children = []
        index += 1


def get_html(url):
    response = requests.get(url)
    return response.text


def buscar_link(html, posicao_inicial=0):
    link_buscar = 'href="http'
    index = html.find(link_buscar, posicao_inicial)
    if index < 0:
        return None, -1

    index += 6
    last_index = html.find('"', index)
    return html[index: last_index], last_index


def buscar_todos_links(url):
    html = get_html(url)
    posicao = 0
    while posicao >= 0:
        link, posicao = buscar_link(html, posicao)
        if posicao >= 0:
            url_children.append(link)


crawler('http://www.uricer.edu.br/site/inicio')