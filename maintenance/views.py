from django.views.generic import TemplateView

class MaintenanceView(TemplateView):
    template_name = "maintenance/maintenance.html"
