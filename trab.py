#!/usr/bin/python3
# -- coding: utf-8 --

from urllib.request import Request, urlopen
import json

MATRICULA = input("Digite sua Matricula")
TOKEN = '0GrRTeQzIh03nn4I6hGqdgI45ksp7hOoft4P0BOGa9jKzqeBQ7N1O4zMZmXHt1gE'
AUTHORIZATION = 'Basic MjAxNDIwMTQwNTAzNjc6ODg0MTQ4OTNpZiM='

req = Request('https://suap.ifrn.edu.br/api/v2/edu/alunos/{}/'.format(MATRICULA))
req.add_header('Accept', 'application/json')
req.add_header('X-CSRFToken', TOKEN)
req.add_header('Authorization', AUTHORIZATION)

dados_byte = urlopen(req).read()
dados_txt = dados_byte.decode('utf-8')
dados_json = dados_byte.decode('utf-8').replace("'", '"')
dados_json = json.loads(dados_json)
print("O seu nome eh " + dados_json['nome'] + ", voce esta " + dados_json['situacao'] + " no Curso " + dados_json['curso'] + " no CAMPUS " + dados_json['campus'])
