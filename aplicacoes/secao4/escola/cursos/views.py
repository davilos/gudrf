from rest_framework import generics
from rest_framework.generics import get_object_or_404

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import mixins
from rest_framework import permissions

from .models import Curso, Avaliacao
from .serializers import CursoSerializer, AvaliacaoSerializer
from .permissions import IsSuperUser

"""
API V1
"""


class CursosAPIView(generics.ListCreateAPIView):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer


class CursoAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer


class AvaliacoesAPIView(generics.ListCreateAPIView):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer

    def get_queryset(self):
        if self.kwargs.get('curso_pk'):
            return self.queryset.filter(curso_id=self.kwargs.get('curso_pk'))
        return self.queryset.all()


class AvaliacaoAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer

    def get_object(self):
        if self.kwargs.get('curso_pk'):
            filter_kwargs = {'curso_id': self.kwargs.get('curso_pk'), 'pk': self.kwargs.get('avaliacao_pk')}
            return get_object_or_404(self.get_queryset(), **filter_kwargs)
            # Pegando uma avaliação de um curso específico
        return get_object_or_404(self.get_queryset(), pk=self.kwargs.get('avaliacao_pk'))


"""
API V2
"""


class CursoViewSet(viewsets.ModelViewSet):
    permission_classes = [IsSuperUser, permissions.DjangoModelPermissions]
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer

    @action(detail=True)
    def avaliacoes(self, request, pk=None):
        """
        Rota para acessar as avaliações de um curso.

        O default do parâmetro methods do decorator action já possui o 'get'.

        Avaliações de um curso específico. Essas avaliações do curso são acessadas através do id do curso.
        O endpoint é: 'cursos/id/avaliacoes/'.
        """
        self.pagination_class.page_size = 1
        avaliacoes = Avaliacao.objects.filter(curso_id=pk)
        page = self.paginate_queryset(avaliacoes)

        self.pagination_class.page_size = 2  # Redefinindo o tamanho da paginação para o padrão

        if avaliacoes.exists():
            serializer = AvaliacaoSerializer(page, many=True)

            return self.get_paginated_response(serializer.data)

        serializer = AvaliacaoSerializer(avaliacoes, many=True)

        return Response(serializer.data)


# class AvaliacaoViewSet(viewsets.ModelViewSet):
#     queryset = Avaliacao.objects.all()
#     serializer_class = AvaliacaoSerializer

class AvaliacaoViewSet(mixins.ListModelMixin,
                       mixins.CreateModelMixin,
                       mixins.RetrieveModelMixin,
                       mixins.UpdateModelMixin,
                       mixins.DestroyModelMixin,
                       viewsets.GenericViewSet
                       ):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer
