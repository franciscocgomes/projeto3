

import requests


# Lendo a página política G1
def page_reader(endereco: str) -> requests.models.Response:
    pagina = requests.get(endereco)
    return pagina



#Gravando o arquivo as informações da variável página
# o Segundo parâmetro w - escrever, r - ler

def grava_pagina_web(resposta: requests.models.Response) -> None:
    arquivo = open("pagina.html", "wb")
    for texto in resposta.iter_content():
        arquivo.write(texto)
    arquivo.close() 



# main

def main():
    endereco = 'https://g1.globo.com/politica/'
    politica = page_reader(endereco)
    grava_pagina_web(politica)


if __name__ == "__main__":
    main()
