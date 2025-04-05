import requests
import json
from time import sleep

NOTICIAS_JOGATINA = "C:\\Users\\WAA-HP\\Documents\\posweb\\servicos_python\\versao4\\noticias\\jogatina.json"
NOTICIAS_SISTEMAS = "C:\\Users\\WAA-HP\\Documents\\posweb\\servicos_python\\versao4\\noticias\\sistemas.json"

URL_SERVICO_JOGATINA = "http://127.0.0.1:5001/gravar"
URL_SERVICO_SISTEMAS = "http://127.0.0.1:5002/gravar"

def enviar(url, noticias):
    sucesso = False
    with open(noticias, "r") as arquivo:
        conteudo = json.load(arquivo)
        noticias = conteudo["noticias"]

        arquivo.close()
        resposta = requests.post(url, json=json.dumps(noticias))
        sucesso = resposta.status_code == 201
    
    return sucesso

if __name__ == "__main__":
    while True:
        sucesso = enviar(URL_SERVICO_JOGATINA, NOTICIAS_JOGATINA)
        if sucesso:
            print("Noticias de jogatina gravadas com sucesso")
        else:
            print("Ocorreu um erro ao gravar as noticias de jogatina")

        sucesso = enviar(URL_SERVICO_SISTEMAS, NOTICIAS_SISTEMAS)
        if sucesso:
            print("Noticias de sistemas gravadas com sucesso")
        else:
            print("Ocorreu um erro ao gravar as noticias de sistemas")
        sleep(10)