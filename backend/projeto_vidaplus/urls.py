from django.urls import path, include


urlpatterns = [
    path('api/auth/', include('apps.usuarios.auth_urls')),
    path('api/unidades/', include('apps.unidades.urls')),
    path('api/profissionais/', include('apps.profissionais.urls')),
    path('api/pacientes/', include('apps.pacientes.urls')),
    path('api/leitos/', include('apps.leitos.urls')),
    path('api/suprimentos/', include('apps.suprimentos.urls')),
    path('api/movimentacoes/', include('apps.movimentacoes.urls')),
    path('api/consultas/', include('apps.consultas.urls')),
    path('api/exames/', include('apps.exames.urls')),
    path('api/internacoes/', include('apps.internacoes.urls')),
]