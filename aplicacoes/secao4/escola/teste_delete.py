import requests

headers = {"Authorization": "Token 668b5a73f4fbfdfdfca4622c4ff66843aa533829"}

url_base_cursos = "http://0.0.0.0:80/api/v2/cursos/"
url_base_avaliacoes = "http://0.0.0.0:80/api/v2/avaliacoes/"

resultado = requests.delete(url=f'{url_base_cursos}12/', headers=headers)

assert resultado.status_code == 204

# Testando se o tamanho do response body é 0
assert len(resultado.text) == 0
