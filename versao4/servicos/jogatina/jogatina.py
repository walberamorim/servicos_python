from flask import Flask, Response, request
from pymemcache.client import base
import json

VERSAO = "3.0.0"

INFO = {
    "descricao": "Servicços que disponibiliza notícias sobre jogos eletrônicos",
    "autor" : "Walber Amorim",
    "versao": VERSAO
}

ALIVE = "sim"

BANCO_DE_NOTICIAS = "bd_jogatina"
PORTA_BANCO_DE_NOTICIAS = 11211

servico = Flask("noticias")

@servico.get("/")
def get():
    return Response(json.dumps(INFO), mimetype="application/json", status=200)

@servico.get("/info")
def get_info():
    return Response(json.dumps(INFO), mimetype="application/json", status=200)

@servico.get("/alive")
def is_alive():
    return Response(ALIVE, mimetype="text/plain", status=200)

@servico.post("/gravar")
def post_jogatina():
    sucesso, noticias = False, request.json
    try:
        cliente = base.Client((BANCO_DE_NOTICIAS, PORTA_BANCO_DE_NOTICIAS))
        cliente.set("jogatina", json.dumps(noticias))
        sucesso = True
        cliente.close()
    except Exception as e:
        print(f"Ocorreu um erro ao salvar as noticias de jogatina: {str(e)}")
    if sucesso:
        return Response(noticias, mimetype="application/json", status=201)
    else:
        return Response(noticias, mimetype="application/json", status=422)

@servico.get("/jogatina")
def get_jogatina():
    sucesso, noticias = False, None
    try:
        cliente = base.Client((BANCO_DE_NOTICIAS, PORTA_BANCO_DE_NOTICIAS))
        noticias = cliente.get("jogatina")
        if noticias is not None:
            noticias = json.loads(noticias.decode("utf-8"))
            sucesso = True
        else:
            noticias = []
        cliente.close()
    except Exception as e:
        print(f"Ocorreu um erro ao obter as noticias de jogatina: {str(e)}")
    if sucesso:
        return Response(noticias, mimetype="application/json", status=200)
    else:
        return Response(noticias, mimetype="application/json", status=204)

if __name__ == "__main__":
    servico.run(host="0.0.0.0", port=5000, debug=True)