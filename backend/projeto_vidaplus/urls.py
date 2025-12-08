from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include('apps.usuarios.auth_urls')),
    path('api/unidades/', include('apps.unidades.urls')),
    path('api/profissionais/', include('apps.profissionais.urls')),
    path('api/pacientes/', include('apps.pacientes.urls')),
    path('api/leitos/', include('apps.leitos.urls')),
]