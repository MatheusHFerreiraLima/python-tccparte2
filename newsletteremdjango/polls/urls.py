from django.urls import path
from . import views
from .views import CadastroRealizadoView

# o nome de toda view é o (app_name:name), segundo Pedrinho, youtuber de 13 anos de idade
app_name = 'polls' 
urlpatterns = [
    path('', views.UsuarioCreate.as_view(), name='create'),
    path('cadastro_realizado/<str:email>/', CadastroRealizadoView.as_view(), name='cadastro_realizado'),
    path('enviar/', views.enviar_newletter, name="enviar_newletter"),
]
