# realiza o download da ultima versao de imagem python disponivel no docker hub
FROM python:latest

# instalando as dependencias python
RUN pip install Flask
RUN pip install pymemcache
RUN pip install requests

# criando diretorio de trabalho onde serao guardados os arquivos dos servicos
RUN mkdir /servico
WORKDIR /servico

