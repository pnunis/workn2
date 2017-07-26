from urllib.request import Request, urlopen
import requests
import json
import getpass
'''
Código python3 para autenticação no SUAP/IFRN. Exemplo de como obter o token para a aplicação.
Prof. Moisés Souto - moises.souto@ifrn.edu.br
Clemente Junior - clemente.ferreira@academico.ifrn.edu.br
O token/ficha e a autorização devem ser obtidos, separadamente, em
    https://suap.ifrn.edu.br/api/docs/
    A url de requisições é: https://suap.ifrn.edu.br/api/v2/
'''
def get_suap_token(username: str, password: str) -> str:
    token = 'token'
    resp = requests.post('https://suap.ifrn.edu.br/api/v2/autenticacao/token/?format=json',json={'username': username, 'password': password})
    payload = resp.json()
    if token in payload.keys():
        return payload[token]
    return ''
username = input("Digite sua matricula:")
senha = getpass.getpass('Senha: ')
TOKEN=get_suap_token(username,senha)
AUTHORIZATION = 'Basic MjAxNDIwMTQwNTA0NTY6UGF1bDE1MjA='
req = Request('https://suap.ifrn.edu.br/api/v2/minhas-informacoes/meus-dados/')
req.add_header('Accept', 'application/json')
req.add_header('X-CSRFToken', TOKEN)
req.add_header('Authorization', AUTHORIZATION)

dados_byte = urlopen(req).read()
dados_json = dados_byte.decode('utf8').replace("'", '"')
dados_json = json.loads(dados_json)
print("Olá "+dados_json['nome_usual']+', o seu e-mail é '+dados_json['email'])
#print("O seu nome eh "+dados_json['nome'] + ", voce esta " + dados_json['situacao'] + " no curso " + dados_json['curso'] + " no CAMPUS " + dados_json['campus'])
