import urllib.request as requisicao
import json
from time import sleep

URL_SERVICO = "http://127.0.0.1:5000/"
URL_JOGATINA = URL_SERVICO + "jogatina"
URL_SISTEMAS = URL_SERVICO + "sistemas"
URL_INFO = URL_SERVICO + "info"

def acessar(url):
    conteudo = None
    try:
        resposta = requisicao.urlopen(url)
        conteudo = resposta.read().decode("utf-8")
    except:
        print(f"Ocorreu um erro ao acessar a url: {url}")
    return conteudo

def get_jogatina():
    noticias = acessar(URL_JOGATINA)
    noticias = json.loads(noticias)
    return noticias

def get_sistemas():
    sistemas = acessar(URL_SISTEMAS)
    sistemas = json.loads(sistemas)
    return sistemas

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
        imprimir_noticias("Jogatina", get_jogatina())
        imprimir_noticias("Sistemas", get_sistemas())
        sleep(5)