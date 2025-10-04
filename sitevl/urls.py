from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("", include("maintenance.urls")),  # 👈 rota principal mostra a página de manutenção
    path("admin/", admin.site.urls),
]
