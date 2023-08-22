from django.contrib import admin
from django.utils.html import mark_safe
from apps.project.models import Crane, Project


# Register your models here.
class CraneAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('crane', 'image', 'title', 'description', 'address')

    @staticmethod
    def html_body_desc(obj):
        # return HTML link that will not be escaped
        return mark_safe(obj.description)


admin.site.register(Crane, CraneAdmin)
admin.site.register(Project, ProjectAdmin)
