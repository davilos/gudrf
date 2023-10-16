from rest_framework import serializers
from django.db.models import Avg

from .models import Curso, Avaliacao


class AvaliacaoSerializer(serializers.ModelSerializer):

    class Meta:
        extra_kwargs = {
            'email': {'write_only': True}
        }
        model = Avaliacao
        fields = (
            'id',
            'curso',
            'nome',
            'email',
            'comentario',
            'avaliacao',
            'criacao',
            'ativo'
        )

    @staticmethod
    def validate_avaliacao(valor):
        if valor in range(1, 6):
            return valor
        raise serializers.ValidationError("A avaliação precisa ser um inteiro entre 1 e 5.")


class CursoSerializer(serializers.ModelSerializer):

    # avaliacoes = AvaliacaoSerializer(many=True, read_only=True)
    # Nested Relationship

    # avaliacoes = serializers. HyperlinkedRelatedField(many=True, read_only=True, view_name='avaliacao-detail')
    # HyperLinked Related Field

    avaliacoes = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    # Primary Key Related Field

    media_avaliacoes = serializers.SerializerMethodField()

    class Meta:
        model = Curso
        fields = (
            'id',
            'titulo',
            'url',
            'criacao',
            'ativo',
            'avaliacoes',
            'media_avaliacoes',
        )

    @staticmethod
    def get_media_avaliacoes(obj):
        media = obj.avaliacoes.aggregate(Avg('avaliacao')).get('avaliacao__avg')

        if media is None:
            return 0
        return round(media * 2) / 2
