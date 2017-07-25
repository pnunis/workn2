#!/usr/bin/python3
# -- coding: utf-8 --

'''
Código python3 para autenticação no SUAP/IFRN. Exemplo de como obter o token para a aplicação.
 pelo usuário https://github.com/jurandysoares
 
O token/ficha e a autorização devem ser obtidos, separadamente, em
    https://suap.ifrn.edu.br/api/docs/
    
No canto superior direito há os botões:
* Django login (necessário para o token);
* e Authorize (necessário para obter a autorização).
'''

from urllib.request import Request, urlopen
import json

MATRICULA = '20142014050456'
TOKEN = 'X-CSRFToken: Wh8UMP4HULtJzFgnlNfVuqffuSYItxEXbHNSFyy23d7XniDU7YQUOU8vgyb8yk9p'
AUTHORIZATION = 'Basic MjAxNDIwMTQwNTA0NTY6UGF1bDE1MjA='

req = Request('https://suap.ifrn.edu.br/api/v2/edu/alunos/{}/'.format(MATRICULA))
req.add_header('Accept', 'application/json')
req.add_header('X-CSRFToken', TOKEN)
req.add_header('Authorization', AUTHORIZATION)

dados_byte = urlopen(req).read()
dados_txt = dados_byte.decode('utf-8')
print(dados_txt)                        
