import requests

headers = {"Authorization": "Token 668b5a73f4fbfdfdfca4622c4ff66843aa533829"}

url_base_cursos = "http://0.0.0.0:80/api/v2/cursos/"
url_base_avaliacoes = "http://0.0.0.0:80/api/v2/avaliacoes/"

novo_curso = {
    "titulo": "Gerência Ágil de Projetos com Scrum",
    "url": "https://www.geekuniversity.com.br/scrum",
}

resultado = requests.post(url=url_base_cursos, headers=headers, data=novo_curso)

# Testando se o curso foi criado com o status code
assert resultado.status_code == 201

# Testando se o título do curso retornado é o mesmo que o do informado
assert resultado.json()['titulo'] == novo_curso['titulo']
