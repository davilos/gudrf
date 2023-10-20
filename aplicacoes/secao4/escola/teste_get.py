import requests

headers = {"Authorization": "Token 668b5a73f4fbfdfdfca4622c4ff66843aa533829"}

url_base_cursos = "http://0.0.0.0:80/api/v2/cursos/"
url_base_avaliacoes = "http://0.0.0.0:80/api/v2/avaliacoes/"

resultado = requests.get(url=url_base_cursos, headers=headers)

# Testando se o endpoint está correto
assert resultado.status_code == 200

# Testando a quantidade de registros
assert resultado.json()['count'] == 6

# Testando se a quantidade de itens está igual ao 'page_size' da paginação
assert len(resultado.json()['results']) == 2

# Testando se o título do primeiro curso está correto
assert resultado.json()['results'][0]['titulo'] == "Programação com JavaScript"
