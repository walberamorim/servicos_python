from flask import Flask, Response
import json

VERSAO = "3.0.0"

INFO = {
    "descricao": "Servicços que disponibiliza notícias sobre jogos eletrônicos",
    "autor" : "Walber Amorim",
    "versao": VERSAO
}

JOGATINA = [
        {
            "id": "1",
            "data": "15/10/2019",
            "titulo": "Stadia, serviço de games na nuvem do Google, será lançado em 19 de Novembro",
            "endereco": "https://g1.globo.com/pop-arte/games/noticia/2019/10/15/stadia-servico-de-games-na-nuvem-do-google-sera-lancado-em-19-de-novembro.ghtml"
        },
        {
            "id": "2",
            "data": "26/04/2019",
            "titulo": "Mortal Kombat: Como fazer todos os fatalities?",
            "endereco": "https://www.uol.com.br/start/ultimas-noticias/2019/04/26/mortal-kombat-11-como-fazer-todas-as-fatalities.htm"
        },
        {
            "id": "3",
            "data": "21/10/2016",
            "titulo": "Conheça 5 distribuições GNU/Linux voltadas para jogos",
            "endereco": "https://sempreupdate.com.br/conheca-5-distribuicoes-gnu-linux-voltadas-para-jogos/"
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

@servico.get("/jogatina")
def get_jogatina():    
    return Response(json.dumps(JOGATINA), mimetype="application/json", status=200)

if __name__ == "__main__":
    servico.run(host="0.0.0.0", port=5000, debug=True)