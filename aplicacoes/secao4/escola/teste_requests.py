import requests


"""
GET Avaliacoes
"""

# avaliacoes = requests.get('http://0.0.0.0:80/api/v2/avaliacoes/')

# Acessando o código de status HTTP
# print(avaliacoes.status_code)

# Acessando os dados do response
# print(avaliacoes.json())
# print(type(avaliacoes.json()))

# Acessando a quantidade de registros
# print(avaliacoes.json()['count'])

# Acessando a próxima página de resultados
# print(avaliacoes.json()['next'])

# Acessando os 'results' dessa página
# print(avaliacoes.json()['results'])

# Acessando o primeiro resultado da lista 'results'
# print(avaliacoes.json()['results'][0])

# Acessando o último resultado da lista 'results'
# print(avaliacoes.json()['results'][-1])

# Acessando o campo 'nome' do último resultado da lista 'results'
# print(avaliacoes.json()['results'][-1]['nome'])


"""
GET Avaliacao
"""

# avaliacao = requests.get('http://0.0.0.0:80/api/v2/avaliacoes/7')
#
# print(avaliacao.json())


"""
GET Cursos
"""

headers = {"Authorization": "Token 668b5a73f4fbfdfdfca4622c4ff66843aa533829"}

cursos = requests.get(url='http://0.0.0.0:80/api/v2/cursos/', headers=headers)

print(cursos.status_code)

print(cursos.json())
