#!/usr/bin/python3
# -- coding: utf-8 --

from urllib.request import Request, urlopen
import requests
import json

'''
Código python3 para autenticação no SUAP/IFRN. Exemplo de como obter o token para a aplicação.
 pelo usuário https://github.com/jurandysoares
 
Prof. Moisés Souto - moises.souto@ifrn.edu.br
Clemente Junior - clemente.ferreira@academico.ifrn.edu.br

O token/ficha e a autorização devem ser obtidos, separadamente, em
    https://suap.ifrn.edu.br/api/docs/
    
No canto superior direito há os botões:
* Django login (necessário para o token);
* e Authorize (necessário para obter a autorização).
'''
#MATRICULA = '20142014050456'
#TOKEN = 'X-CSRFToken: Wh8UMP4HULtJzFgnlNfVuqffuSYItxEXbHNSFyy23d7XniDU7YQUOU8vgyb8yk9p'
#AUTHORIZATION = 'Basic MjAxNDIwMTQwNTA0NTY6UGF1bDE1MjA='


def get_suap_token(username: str, password: str) -> str:
    token = 'token'
    resp = requests.post('https://suap.ifrn.edu.br/api/v2/autenticacao/token/?format=json',json={'username': username, 'password': password})
    payload = resp.json()
    print(payload)
    if token in payload.keys():
        return payload[token]
    return ''
username = input("Digite sua matricula:")
senha = input("Digite sua senha:")
TOKEN=get_suap_token(username,senha)
AUTHORIZATION = 'Basic MjAxNDIwMTQwNTAzNjc6ODg0MTQ4OTNpZiM='

req = Request('https://suap.ifrn.edu.br/api/v2/minhas-informacoes/meus-dados/')
req.add_header('Accept', 'application/json')
req.add_header('X-CSRFToken', TOKEN)
req.add_header('Authorization', AUTHORIZATION)

dados_byte = urlopen(req).read()
dados_json = dados_byte.decode('utf8').replace("'", '"')
dados_json = json.loads(dados_json)
dados_txt = dados_byte.decode('utf-8')
print("O seu nome "+dados_json['nome'] + ", sua situacao " + dados_json['situacao'] + " esta cursando " + dados_json['curso'] + " no CAMPUS " + dados_json['campus'])

