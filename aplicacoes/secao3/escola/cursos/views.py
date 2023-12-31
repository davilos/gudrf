from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Curso, Avaliacao
from .serializers import CursoSerializer, AvaliacaoSerializer


class CursoAPIView(APIView):
    """
    API de Cursos da Geek University.
    """
    @staticmethod
    def get(request):
        cursos = Curso.objects.all()
        serializer = CursoSerializer(cursos, many=True)

        return Response(serializer.data)

    @staticmethod
    def post(request):
        serializer = CursoSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class AvaliacaoAPIView(APIView):
    """
    API de Avaliações dos cursos da Geek University.
    """
    @staticmethod
    def get(request):
        avaliacoes = Avaliacao.objects.all()
        serializer = AvaliacaoSerializer(avaliacoes, many=True)

        return Response(serializer.data)

    @staticmethod
    def post(request):
        serializer = AvaliacaoSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)
