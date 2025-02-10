from django.contrib import admin

from .models import Registrar, Domain

@admin.register(Registrar)
class RegistrarAdmin(admin.ModelAdmin):
    pass

@admin.register(Domain)
class DomainAdmin(admin.ModelAdmin):
    pass