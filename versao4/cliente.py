import urllib.request as requisicao
import json
from time import sleep

URL_SERVICO_JOGATINA = "http://127.0.0.1:5001/"
URL_SERVICO_SISTEMAS = "http://127.0.0.1:5002/"
URL_JOGATINA = URL_SERVICO_JOGATINA + "jogatina"
URL_SISTEMAS = URL_SERVICO_SISTEMAS + "sistemas"
URL_ALIVE_JOGATINA = URL_SERVICO_JOGATINA + "alive"
URL_ALIVE_SISTEMAS = URL_SERVICO_SISTEMAS + "alive"

def acessar(url):
    sucesso, conteudo = False, None
    try:
        resposta = requisicao.urlopen(url)
        if resposta.status == 200:
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
    return sucesso, noticias

def get_sistemas():
    sucesso, sistemas = acessar(URL_SISTEMAS)
    if sucesso:
        sistemas = json.loads(sistemas)
    else:
        print(f"Ocorreu um erro ao obter as noticias")
    return sucesso, sistemas

def servico_jogatina_ativo():
    sucesso, ativo = acessar(URL_ALIVE_JOGATINA)
    return sucesso and ativo == "sim"

def servico_sistemas_ativo():
    sucesso, ativo = acessar(URL_ALIVE_SISTEMAS)
    return sucesso and ativo == "sim"

def imprimir_noticias(tipo_noticias, noticias):
    print(f"Imprimindo noticias sobre {tipo_noticias}")
    for contador, noticia in enumerate(noticias):
        print(f"Noticia {contador}")
        print(f"ID: {noticia['id']}")
        print(f"Data: {noticia['data']}")
        print(f"Titulo: {noticia['titulo']}")
        print(f"Endereço: {noticia['endereco']}")
        print("\n")

if __name__ == "__main__":
    while True:
        if servico_jogatina_ativo():
            sucesso, noticias = get_jogatina()
            tipo = "jogatina"
            if sucesso:
                imprimir_noticias(tipo, noticias)
            else:
                print(f"Ocorreu um erro ao obter as noticias de {tipo}")
        else:
            print("Nenhum servico ativo")
        if servico_sistemas_ativo():
            sucesso, noticias = get_sistemas()
            tipo = "sistemas"
            if sucesso:
                imprimir_noticias(tipo, noticias)
            else:
                print(f"Ocorreu um erro ao obter as noticias de {tipo}")
        else:
            print("Nenhum servico ativo")
        sleep(5)