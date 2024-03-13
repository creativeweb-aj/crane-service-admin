from django.apps import AppConfig


class WorkManagementConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.work_management'

    def ready(self):
        import apps.work_management.signals
