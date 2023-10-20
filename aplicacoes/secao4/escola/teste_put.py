import requests

headers = {"Authorization": "Token 668b5a73f4fbfdfdfca4622c4ff66843aa533829"}

url_base_cursos = "http://0.0.0.0:80/api/v2/cursos/"
url_base_avaliacoes = "http://0.0.0.0:80/api/v2/avaliacoes/"

curso_atualizado = {
    "titulo": "Novo Curso de Scrum 2",
    "url": "https://www.geekuniversity.com.br/ncs2"
}

# Buscando o curso com o id 12
# curso = requests.get(url=f'{url_base_cursos}12/', headers=headers)
# print(curso.json())

resultado = requests.put(url=f'{url_base_cursos}12/', headers=headers, data=curso_atualizado)

assert resultado.status_code == 200

assert resultado.json()['titulo'] == curso_atualizado['titulo']
