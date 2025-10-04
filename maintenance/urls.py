from django.urls import path
from .views import MaintenanceView

urlpatterns = [
    path("", MaintenanceView.as_view(), name="maintenance"),
]
