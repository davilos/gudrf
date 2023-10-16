import requests
import jsonpath


avaliacoes = requests.get('http://0.0.0.0:80/api/v2/avaliacoes/')

# results = jsonpath.jsonpath(avaliacoes.json(), 'results')
# print(results)

# primeiro = jsonpath.jsonpath(avaliacoes.json(), 'results[0]')
# print(primeiro)

# nome = jsonpath.jsonpath(avaliacoes.json(), 'results[0].nome')
# print(nome)

# nota_data = jsonpath.jsonpath(avaliacoes.json(), 'results[0].avaliacao')
# print(nota_data)

# curso_id = jsonpath.jsonpath(avaliacoes.json(), 'results[0].curso')
# print(curso_id)

# Todos as avaliações das pessoas que avaliaram o curso
headers = {"Authorization": "Token 668b5a73f4fbfdfdfca4622c4ff66843aa533829"}
base_url = 'http://0.0.0.0:80/api/v2/cursos/6/avaliacoes/'

notas = []

next_page = base_url
while next_page:
    response = requests.get(next_page, headers=headers)
    data = response.json()

    # O tamanho da paginação do endpoint é 1
    nota_pagina = jsonpath.jsonpath(data, 'results[*].avaliacao')
    notas.extend(nota_pagina)

    next_page = data.get('next')

print(notas)
