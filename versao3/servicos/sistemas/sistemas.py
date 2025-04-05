from flask import Flask, Response
import json

VERSAO = "3.0.0"

INFO = {
    "descricao": "Servicços que disponibiliza notícias sobre sistemas operacionais",
    "autor" : "Walber Amorim",
    "versao": VERSAO
}

SISTEMAS = [
        {
            "id": "1",
            "data": "22/05/2019",
            "titulo": "Estes são os 12 problemas já encontrados na atualização do Windows 10",
            "endereco": "https://olhardigital.com.br/noticia/microsoft-lista-todos-os-problemas-da-nova-atualizacao-do-windows-10/86052"
        },
        {
            "id": "2",
            "data": "10/05/2015",
            "titulo": "Atualização do Windows 10 está causando problemas para alguns usuários",
            "endereco": "https://canaltech.com.br/windows/atualizacao-do-windows-10-esta-causando-problemas-para-alguns-usuarios-46921/"
        },
        {
            "id": "3",
            "data": "04/05/2016",
            "titulo": "Top 5 distribuições Linux que podem substituir o Windows 10",
            "endereco": "https://pplware.sapo.pt/linux/top-5-distribuies-gnulinux-que-podem-substituir-o-windows-10/"
        }
    ]

ALIVE = "sim"

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

@servico.get("/sistemas")
def get_sistemas():    
    return Response(json.dumps(SISTEMAS), mimetype="application/json", status=200)

if __name__ == "__main__":
    servico.run(host="0.0.0.0", port=5000, debug=True)