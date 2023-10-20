import requests


class TestCursos:
    headers = {"Authorization": "Token 668b5a73f4fbfdfdfca4622c4ff66843aa533829"}
    url_base_cursos = "http://0.0.0.0:80/api/v2/cursos/"

    def test_get_cursos(self):
        cursos = requests.get(url=self.url_base_cursos, headers=self.headers)

        assert cursos.status_code == 200

    def test_get_curso(self):
        curso = requests.get(url=f'{self.url_base_cursos}6/', headers=self.headers)

        assert curso.status_code == 200

    def test_post_curso(self):
        novo_curso = {
            "titulo": "Curso de Programação com Ruby",
            "url": "https://www.geekuniversity.com.br/cpr",
        }

        response = requests.post(url=self.url_base_cursos, headers=self.headers, data=novo_curso)

        assert response.status_code == 201

        assert response.json()['titulo'] == novo_curso['titulo']

    def test_put_curso(self):
        curso_atualizado = {
            "titulo": "Novo Curso de Ruby",
            "url": "https://www.geekuniversity.com.br/ncr"
        }

        response = requests.put(url=f'{self.url_base_cursos}13/', headers=self.headers, data=curso_atualizado)

        assert response.status_code == 200

        assert response.json()['titulo'] == curso_atualizado['titulo']

    def test_patch_curso(self):
        curso_atualizado = {
            "titulo": "Novo Curso de Ruby com PATCH"
        }

        response = requests.patch(url=f'{self.url_base_cursos}13/', headers=self.headers, data=curso_atualizado)

        assert response.status_code == 200

        assert response.json()['titulo'] == curso_atualizado['titulo']
        assert not response.json()['url'] == ""

    def test_delete_curso(self):
        response = requests.delete(url=f'{self.url_base_cursos}13/', headers=self.headers)

        assert response.status_code == 204 and len(response.text) == 0
