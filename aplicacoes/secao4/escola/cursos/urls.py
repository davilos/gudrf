from django.urls import path

from . import views

urlpatterns = [
    path('cursos/', views.CursosAPIView.as_view(), name='cursos'),
    path('cursos/<int:pk>/', views.CursoAPIView.as_view(), name='curso'),
    path('cursos/<int:curso_pk>/avaliacoes/', views.AvaliacoesAPIView.as_view(), name='curso_avaliacoes'),
    path('cursos/<int:curso_pk>/avaliacoes/<int:avaliacao_pk>/', views.AvaliacaoAPIView.as_view(),
         name='curso_avaliacao'),

    path('avaliacoes/', views.AvaliacoesAPIView.as_view(), name='avaliacoes'),
    path('avaliacoes/<int:avaliacao_pk>/', views.AvaliacaoAPIView.as_view(), name='avaliacao'),
]
