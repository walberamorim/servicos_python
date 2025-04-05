import urllib.request as requisicao
import json
from time import sleep

URL_SERVICO = "http://127.0.0.1:5000/"
URL_JOGATINA = URL_SERVICO + "jogatina"
URL_SISTEMAS = URL_SERVICO + "sistemas"
URL_INFO = URL_SERVICO + "info"
URL_ALIVE = URL_SERVICO + "alive"

def acessar(url):
    sucesso, conteudo = False, None
    try:
        resposta = requisicao.urlopen(url)
        conteudo = resposta.read().decode("utf-8")
        sucesso = True
    except:
        print(f"Ocorreu um erro ao acessar a url: {url}")
    return sucesso, conteudo

def get_jogatina():
    sucesso, noticias = acessar(URL_JOGATINA)
    if sucesso:
        noticias = json.loads(noticias)
    else:
        print(f"Ocorreu um erro ao obter as noticias")
    return noticias

def get_sistemas():
    sucesso, sistemas = acessar(URL_SISTEMAS)
    if sucesso:
        sistemas = json.loads(sistemas)
    else:
        print(f"Ocorreu um erro ao obter as noticias")
    return sistemas

def servico_ativo():
    sucesso, ativo = acessar(URL_ALIVE)
    return sucesso and ativo == "sim"

def imprimir_noticias(tipo_noticias, noticias):
    print(f"Imprimindo noticias sobre {len(tipo_noticias)}")
    for contador, noticia in enumerate(noticias):
        print(f"Noticia {contador}")
        print(f"ID: {noticia['id']}")
        print(f"Data: {noticia['data']}")
        print(f"Titulo: {noticia['titulo']}")
        print(f"Endereço: {noticia['endereco']}")
        print("\n")

if __name__ == "__main__":
    while True:
        if servico_ativo():
            imprimir_noticias("Jogatina", get_jogatina())
            imprimir_noticias("Sistemas", get_sistemas())
            sleep(5)
        else:
            print("Servico inativo")
            sleep(5)